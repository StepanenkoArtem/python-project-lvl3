# coding=utf-8

"""Configure logging."""

import logging


class LoggingError(Exception):
    """Logging Error exception."""

    def __init__(self, message):
        """Init Logging Exception.

        Args:
            message: str
                Exception's message
        """
        self.exit_code = 3
        self.message = message

    def __str__(self):
        """Provide user-friendly message about error.

        Returns:
            message : (str)
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
