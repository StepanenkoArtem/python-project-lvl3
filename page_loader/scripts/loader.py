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

config.dictConfig(logconf.dict_config)

logger = logging.getLogger(logconf.DEFAULT_LOGGER)


def _validate_loglevel(ctx, _, level):
    try:
        logger.setLevel(level.upper())
    except AttributeError:
        logger.setLevel(level)
    except ValueError:
        logger.warning(
            'Uknown logging level `{lvl}`. Using default {default_lvl}'.format(
                lvl=level,
                default_lvl=logger.level,
            ),
        )


def _validate_logfile(ctx, _, logfile):
    if logfile:
        try:
            custom_file_handler = logging.FileHandler(logfile)
        except PermissionError as perm_error:
            logger.warning(perm_error)
        finally:
            custom_file_handler.setFormatter(
                logging.Formatter(
                    logconf.VERBOSE_FORMAT,
                ),
            )
            logger.addHandler(custom_file_handler)


@click.command()
@click.option(
    '--output',
    default=join(os.getcwd(), settings.DEFAULT_DOWNLOAD_DIR),
    help='Set destionation folder to save file',
)
@click.option(
    '--loglevel',
    callback=_validate_loglevel,
    help='Set logging level (INFO, DEBUG, WARNING, ERROR or CRITICAL)',
)
@click.option(
    '--logfile',
    help='Set logfile path',
    callback=_validate_logfile,
)
@click.argument(
    'url',
)
def main(url, output, loglevel, logfile):
    """Download URL page."""
    logger.info('Start new job')
    try:
        localize(download.download(url), output)
    except (PermissionError, FileNotFoundError):
        sys.exit(settings.EXIT_FS_ERR)
    except (ConnectionError, TimeoutError):
        sys.exit(settings.EXIT_CON_ERR)


if __name__ == '__main__':
    main()
