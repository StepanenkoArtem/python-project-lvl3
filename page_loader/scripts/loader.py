#!/usr/bin/env python
# coding=utf-8

"""Main module. Retrive url from command line args."""

import logging
import sys
from logging import config
from os import getcwd
from os.path import join

import click
import yaml
from page_loader import download, settings
from page_loader.localize import localize

with open(settings.LOG_CONF) as config_file:
    config_dict = yaml.safe_load(config_file)
config.dictConfig(config_dict)

logger = logging.getLogger(settings.DEFAULT_LOGGER)


@click.command()
@click.option(
    '--output',
    default=join(getcwd(), settings.DEFAULT_DOWNLOAD_DIR),
    help='Set destionation folder to save file',
)
@click.option(
    '--loglevel',
    type=str,
    default=logger.level,
    help='Set logging level',
)
@click.option(
    '--logpath',
    help='Set logfile path',
)
@click.argument(
    'url',
)
def main(url, output, loglevel, logpath):
    """Entry point."""
    logger.setLevel(loglevel)
    if logpath:
        try:
            custom_handler = logging.FileHandler(logpath)
        except PermissionError:
            logger.error(settings.ERR_FS_PERMISSION_DND)
            sys.exit(settings.EXIT_FS_ERR)

        custom_handler.setFormatter(
            logging.Formatter(settings.DEFAULT_FORMATTER, style='{'),
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
