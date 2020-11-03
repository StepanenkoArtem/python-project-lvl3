#!/usr/bin/env python
# coding=utf-8

"""Main module."""

import logging
import sys

from loader import cli, logger, network, storage

if __name__ == '__main__':
    try:
        cli.main()
    except (
        cli.ParamError,
        logger.LoggingError,
        network.NetworkError,
        storage.StorageError,
    ) as error:
        logging.error(error)
        logging.debug(error.__cause__)
        sys.exit(error.exit_code)
