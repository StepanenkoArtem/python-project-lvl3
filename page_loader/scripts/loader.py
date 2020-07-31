#!/usr/bin/env python
# coding=utf-8

"""Main module. Retrive url from command line args."""
import logging
import os
import sys
from logging import config
from os.path import join

import click
from page_loader import download, logconf, settings
from page_loader.localize import localize

config.dictConfig(logconf.config_dict)

logger = logging.getLogger(logconf.DEFAULT_LOGGER)


@click.command()  # noqa: WPS213
@click.option(
    '--output',
    default=join(os.getcwd(), settings.DEFAULT_DOWNLOAD_DIR),
    help='Set destionation folder to save file',
)
@click.option(
    '--loglevel',
    type=str,
    default=logger.level,
    help='Set logging level (INFO, DEBUG, WARNING, ERROR or CRITICAL)',
)
@click.option(
    '--logpath',
    help='Set logfile path',
)
@click.argument(
    'url',
)
def main(url, output, logpath, loglevel):
    """Download URL page."""
    try:
        logger.setLevel(loglevel.upper())
    except ValueError as uknown_level:
        logger.warning(uknown_level)

    if logpath:
        try:
            custom_handler = logging.FileHandler(logpath)
        except PermissionError:
            logger.error(logconf.ERR_FS_PERMISSION_DND)
            sys.exit(settings.EXIT_FS_ERR)

        custom_handler.setFormatter(
            logging.Formatter(logconf.VERBOSE_FORMAT),
        )
        logger.addHandler(custom_handler)
    try:
        localize(download.download(url), output)
    except (PermissionError, FileNotFoundError):
        sys.exit(settings.EXIT_FS_ERR)
    except (ConnectionError, TimeoutError):
        sys.exit(settings.EXIT_CON_ERR)


if __name__ == '__main__':
    main()
