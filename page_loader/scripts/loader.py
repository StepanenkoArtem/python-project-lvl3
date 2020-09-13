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

# Exit codes
EXIT_CON_ERR = 1
EXIT_FS_ERR = 2
EXIT_PARAM_ERR = 3

config.dictConfig(logconf.dict_config)

logger = logging.getLogger(logconf.DEFAULT_LOGGER)


def _validate_loglevel(ctx, param, level):  # noqa: WPS110
    try:
        logger.setLevel(level)
    except ValueError:
        logger.critical('Uknown logging level `{lvl}`'.format(lvl=level))
        raise ValueError


def _validate_logfile(ctx, param, logfile):  # noqa: WPS110
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
@ click.option(
    '--loglevel',
    callback=_validate_loglevel,
    help='Set logging level (INFO, DEBUG, WARNING, ERROR or CRITICAL)',
    default='DEBUG',
)
@click.option(
    '--logfile',
    help='Set logfile path',
    callback=_validate_logfile,
)
@click.argument(
    'url',
)
def main(url, output, logfile, loglevel):
    """Download URL page."""
    logger.info('Start new job')
    try:
        localize(download.download(url), output)
    except (PermissionError, FileNotFoundError):
        sys.exit(EXIT_FS_ERR)
    except (ConnectionError, TimeoutError):
        sys.exit(EXIT_CON_ERR)
    except (ValueError):
        sys.exit(EXIT_PARAM_ERR)


if __name__ == '__main__':
    main()
