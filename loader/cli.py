# coding=utf-8

"""Commandline module."""
import logging
import os
import sys
from urllib.parse import urlparse, urlunsplit

import click
from bs4 import BeautifulSoup
from tqdm import tqdm
import loader

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


def check_level(ctx, param, value):
    """Validate logging level argument.

    Args:
        ctx: click context
        param : parameter object
        value : parameter 'loglevel' value

    Returns:
        : int
            valid logging level
    """
    try:
        return int(value)
    except ValueError:
        return value.upper()


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
            '{value} for "--{param}" is not permitted'.format(
                value=value, param=param,
            ),
        ) from PermissionError
    return abs_path


@click.command()
@click.option(
    '--output',
    default=os.path.join(os.getcwd(), 'downloads'),
    help='Set destionation folder to save file',
    callback=check_path,
)
@click.option(
    '--loglevel',
    type=str,
    help='Set logging level (INFO, DEBUG, WARNING, ERROR or CRITICAL)',
    default=logging.WARNING,
    callback=check_level,
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
    loader.logging.setup(level=loglevel, logfile=logfile)

    # Download page and get DOM
    dom = BeautifulSoup(loader.network.download(url), DEFAULT_PARSER)

    # Split URL to fragments
    scheme, net_loc, *_ = list(urlparse(url))

    # Get resource objects from DOM
    resources = loader.handler.get_resources(dom)

    if resources:
        # Build resource dirname
        local_dirname = loader.path.for_resource_dir(url)
        # Create dir for resource inside 'output'
        loader.storage.mkdir(os.path.join(output, local_dirname))

        web_resource_paths = []
        for resource in resources:
            # Get resource path from resource object
            web_resource_path = loader.handler.get_path(resource)
            # Build resource local path
            local_resource_path = os.path.join(
                local_dirname,
                loader.path.for_resource(web_resource_path),
            )
            # Set local path in resource object
            loader.handler.update_resource(
                resource=resource,
                new_link=local_resource_path,
            )
            web_resource_paths.append(web_resource_path)
        # Save modified DOM
        loader.storage.save(
            f_content=dom.encode(),
            output=output,
            filename=loader.path.for_page(url),
        )
        # Download resources
        for resource_path in tqdm(web_resource_paths, desc=BAR_DESC):
            resource_url = urlunsplit(
                [scheme, net_loc, resource_path, None, None],
            )
            try:
                loader.storage.save(
                    f_content=loader.network.download(resource_url),
                    output=os.path.join(output, local_dirname),
                    filename=loader.path.for_resource(resource_path),
                )
            except loader.network.NetworkError as error:
                logging.debug(error, exc_info=sys.exc_info())
