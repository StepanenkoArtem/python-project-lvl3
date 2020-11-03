# coding=utf-8

"""Commandline module."""
import logging
import os
import traceback
from urllib.parse import urlparse, urlunparse

import click
from bs4 import BeautifulSoup
from tqdm import tqdm
from loader import handler, logger, network, path, storage

DEFAULT_PARSER = 'html.parser'
BAR_DESC = 'LOAD RESOURCES'


class ParamError(Exception):
    """Wrong Parameter Exception."""

    def __init__(self, message):
        """Init ParamError.

        Args:
            message : str
                Parameter error message
        """
        self.message = message
        self.exit_code = 4

    def __str__(self):
        """Provide user-friendly message.

        Returns:
            str: Error message
        """
        return self.message


def check_path(ctx, param, value):
    """Check is 'output' argument valid.

    Args:
        ctx: click context
        param : parameter object
        value : parameter 'output' value

    Returns:
        str : path to output directory

    Raises:
        ParamError : if output directory permission denied
    """
    abs_path = os.path.abspath(os.path.expanduser(value))
    if not os.access(os.path.dirname(abs_path), os.W_OK):
        raise ParamError(
            '{value} for {param} is not permitted'.format(
                value=value, param=param,
            ),
        ) from PermissionError
    return value


@click.command()
@click.option(
    '--output',
    default=os.path.join(os.getcwd(), 'downloads'),
    help='Set destionation folder to save file',
    callback=check_path,
)
@click.option(
    '--loglevel',
    help='Set logging level (INFO, DEBUG, WARNING, ERROR or CRITICAL)',
    default=logging.WARNING,
)
@click.option(
    '--logfile',
    help='Set logfile path',
    default='loader.log',
    callback=check_path,
)
@click.argument(
    'url',
)
def run(url, output, loglevel, logfile):
    """Run user's input command.

    Args:
        url : str
            Requested url
        output : str
            Path to save downloaded page
        loglevel : (str|int)
            Logging level
        logfile : str
            Custom logfile name
    """
    # Logging setup
    logger.setup(level=loglevel, logfile=logfile)

    # Download page and get DOM
    dom = BeautifulSoup(network.download(url), DEFAULT_PARSER)

    # Get resource objects from DOM
    resources = handler.get_resources(dom)

    # Split URL to fragments
    url_parts = list(urlparse(url))

    if resources:
        # Build resource dirname
        resource_dirname = path.for_resource_dir(url)
        # Create dir for resource inside 'output'
        storage.mkdir(os.path.join(output, resource_dirname))

        resource_urls = []
        for resource in resources:
            # Get resource path from resource object
            resource_path = handler.get_path(resource)
            # Build resource filename
            resource_filename = path.for_resource(resource_path)

            # Set local path in resource object
            handler.update_resource(
                resource=resource,
                new_link=os.path.join(resource_dirname, resource_filename),
            )
            # Build URL for resource
            url_parts[2] = resource_path
            resource_urls.append(urlunparse(url_parts))

        # Save modified DOM
        storage.save(
            f_content=dom.encode(),
            output=output,
            filename=path.for_page(url),
        )
        # Download resources and save it
        for resource_url in tqdm(resource_urls, desc=BAR_DESC):
            try:
                storage.save(
                    f_content=network.download(resource_url),
                    output=os.path.join(output, resource_dirname),
                    filename=resource_filename,
                )
            except network.NetworkError:
                logging.debug(
                    traceback.format_exception_only(network.NetworkError),
                )
