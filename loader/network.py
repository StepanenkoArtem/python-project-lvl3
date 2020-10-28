# coding=utf-8

"""Retrive URL resource."""

import requests


class NetworkError(Exception):
    """Network Error Exceptions."""

    def __init__(self, message):
        """Define NetworkError Exception.

        Args:
            message: str
                Exception's message
        """
        self.exit_code = 1
        self.message = message

    def __str__(self):
        """Show message while exception is logging.

        Returns:
            message : (str)
        """
        return self.message


def download(url):
    """
    Download requested url.

    Args:
        url : (str) Url address specified from command-line args

    Returns:
        downloaded : (bytes) Content of downloaded page

    Raises:
        NetworkError : Cannot establish connection to host
    """
    try:  # noqa: WPS229
        requested = requests.get(
            url=url,
            timeout=3,
        )
        requested.raise_for_status()
    except (
        requests.RequestException,
        requests.exceptions.HTTPError,
    ) as request_err:
        raise NetworkError(
            message="Can't connect to {url}".format(url=url),
        ) from request_err

    return requested.content
