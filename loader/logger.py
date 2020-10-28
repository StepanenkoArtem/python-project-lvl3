# coding=utf-8

"""Confiuring logging."""

import logging
import logging.config  # noqa: WPS301


def setup(level, logfile):
    """Set up logging settings.

    Args:
        level : (int) logging level
        logfile : (str) logfile name
    """
    # Configure console handler
    console_formatter = logging.Formatter(
        fmt='{levelname}:{message}',
        style='{',
    )
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(console_formatter)

    #  Configure file handler
    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        fmt='{asctime}:{levelname}:{message}',
        style='{',
    )
    file_handler.setFormatter(file_formatter)

    logging.basicConfig(
        handlers=(console_handler, file_handler),
        level=logging.DEBUG,
    )
