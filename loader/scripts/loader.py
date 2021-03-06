#!/usr/bin/env python
# coding=utf-8

"""Main module."""

import logging
import sys

from loader import cli, logger


def main():
    """Run main function."""
    try:
        cli.run()
    except (
        cli.ParamError,
        logger.LoaderBasicException,
    ) as error:
        logging.error(error)
        logging.debug(error.__cause__)
        sys.exit(error.exit_code)


if __name__ == '__main__':
    main()
