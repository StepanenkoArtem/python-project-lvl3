# coding=utf-8

"""Confiuring logging."""

import logging
import logging.config


def setup(
    level=logging.WARNING,
    logfile='loader.log',
):
    """Setup logging settings."""
    # Configure console handler
    console_formatter = logging.Formatter(
        fmt='{levelname}:{message}',
        style='{',
    )
    console_handler = logging.StreamHandler
    console_handler.setLevel(level)
    console_handler.setFormatter(console_formatter)

    #  Configure file handler
    file_handler = logging.FileHandler(logfile)
    file_formatter = logging.Formatter(
        fmt='{asctime}:{levelname}:{name}:{message}',
        style='{',
    )
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.DEBUG)

    logging.basicConfig(
        handlers=(console_handler, file_handler),
    )
