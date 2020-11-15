# coding=utf-8

"""Configure logging."""

import logging


class LoaderBasicException(Exception):
    """Logging Error exception."""

    exit_code: int = None

    def __init__(self, message):
        """Init Logging Exception.

        Args:
            message: str
                Exception's message
        """
        super().__init__()
        self.message = message

    def __str__(self):
        """Provide user-readable message.

        Returns:
            str: Exception's message
        """
        return self.message


def setup(level, logfile):
    """Set up logging settings.

    Args:
        level : (int|str) logging level
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
