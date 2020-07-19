#!/usr/bin/env python
# coding=utf-8

"""Main module. Retrive url from command line args."""

import logging
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

logger = logging.getLogger(__package__)


@click.command()
@click.option(
    '--output',
    default=join(getcwd(), settings.DEFAULT_DOWNLOAD_DIR),
    help='Set destionation folder to save file',
)
@click.option(
    '--log',
    type=str,
    default=logger.level,
    help='Set logging level',
)
@click.option(
    '--logfile',
    help='Set logfile path',
)
@click.argument(
    'url',
)
def main(url, output, log, logfile):
    """Entry point."""
    logger.setLevel(log)
    if logfile:
        custom_handler = logging.FileHandler(logfile)
        logger.addHandler(custom_handler)
    localize(download.download(url), output)


if __name__ == '__main__':
    main()
