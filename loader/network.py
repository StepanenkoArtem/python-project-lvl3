# coding=utf-8

"""Retrive URL resource."""

import requests
from loader.logging import LoaderBasicException


class NetworkError(LoaderBasicException):
    """Network Error Exception."""

    exit_code = 3

    def __init__(self, message):
        """Init Network Exception.

        Args:
            message (str): message error
        """
        self.message = message


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
