# coding=utf-8

import logging
import os
import sys
from os.path import join

import click
from loader import handler, logger, network, path, storage

# Exit codes
EXIT_CONNECTION_ERR = 1
EXIT_FILESYSTEM_ERR = 2
EXIT_PARAM_ERR = 3


@click.command()
@click.option(
    '--output',
    default=join(os.getcwd(), 'downloads'),
    help='Set destionation folder to save file',
)
@ click.option(
    '--loglevel',
    help='Set logging level (INFO, DEBUG, WARNING, ERROR or CRITICAL)',
    default='DEBUG',
)
@click.option(
    '--logfile',
    help='Set logfile path',
)
@click.argument(
    'url',
)
def main(url, output, level, logfile):
    logger.setup(
        level=level,
        logfile=logfile,
    )

    # Download page
    try:
        page = network.get_page(url)
    except network.NetworkError:
        logging.error()
        sys.exit(EXIT_CONNECTION_ERR)

    # Save modified page
    try:
        storage.save(
            content=handler.set_local_links(page),
            filename=path.for_page(url),
            output=output,
        )
    except storage.StorageError:
        sys.exit(EXIT_FILESYSTEM_ERR)

    resource_links = handler.get_links(page)

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
        except network.NetworkError:
            logging.error('')

        # Save downoaded resource
        try:
            storage.save(
                content=resource,
                filename=path.for_resource(link),
                output=resource_dir,
            )
        except storage.StorageError:
            logging.error('')
