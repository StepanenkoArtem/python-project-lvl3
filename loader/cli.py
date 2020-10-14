# coding=utf-8

"""Checking are commandline arguments valid."""
import logging
import os
import sys
from os.path import join

import click
from loader import handler, network, path, storage

# Exit codes
EXIT_CONNECTION_ERR = 1
EXIT_FILESYSTEM_ERR = 2
EXIT_PARAM_ERR = 3


VERBOSE_FORMAT = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
SIMPLE_FORMAT = '%(levelname)s:%(message)s'


def check_level(ctx, _, level):
    """Check logging level commandline argument."""
    try:
        logging.get_logger.setLevel(level)
    except ValueError:
        logging.critical('Uknown logging level `{lvl}`'.format(lvl=level))
        raise ValueError


def check_file(ctx, _, logfile):
    if logfile:
        try:
            custom_file_handler = logging.FileHandler(logfile)
        except PermissionError as perm_error:
            logging.warning(perm_error)
        finally:
            custom_file_handler.setFormatter(
                logging.Formatter(
                    VERBOSE_FORMAT,
                ),
            )
            logging.addHandler(custom_file_handler)


@click.command()
@click.option(
    '--output',
    default=join(os.getcwd(), 'downloads'),
    help='Set destionation folder to save file',
)
@ click.option(
    '--loglevel',
    callback=check_level,
    help='Set logging level (INFO, DEBUG, WARNING, ERROR or CRITICAL)',
    default='DEBUG',
)
@click.option(
    '--logfile',
    help='Set logfile path',
    callback=check_file,
)
@click.argument(
    'url',
)
def main(url, output, level, logfile):
    """
    """
    # Download page
    try:
        page = network.get_page(url)
    except NetworkError:
        sys.exit(EXIT_CONNECTION_ERR)

    # Get resource links
    resource_links = handler.get_links(page)

    # Replace origin resource links to local paths
    page = handler.set_local_links(page)

    # Save modified page
    try:
        storage.save(
            content=page,
            filename=path.for_page(url),
            output=output,
        )
    except StorageError:
        sys.exit(EXIT_FILESYSTEM_ERR)

    # Make dirname for downloaded resource
    if resource_links:
        resource_dir = '{destination}{postfix}'.format(
            destination=output,
            postfix='_files',
        )
        for link in resource_links:

            # Download resources
            try:
                resource = network.get_page(link)
            except NetworkError:
                logging.error('')

            # Save downoaded resource
            try:
                storage.save(
                    content=resource,
                    filename=path.for_resource(link),
                    output=resource_dir,
                )
            except StorageError:
                logging.error('')
