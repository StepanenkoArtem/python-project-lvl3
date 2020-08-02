# coding=utf-8

"""Retrive URL resource."""

import logging

import requests
from page_loader import settings
from page_loader.localize import url_normalize

logger = logging.getLogger(__name__)


def download(url):
    """
    Download requested url.

    Args:
        url : str
            Url address specified from command-line args

    Returns:
        downloaded : <requests.object>

    Raises:
        ConnectionError : Cannot establish connection to host
    """
    logger.debug('Trying to download {url}'.format(url=url))
    try:
        requested = requests.get(
            url=url_normalize(url),
            timeout=settings.DEFAULT_TIMEOUT,
        )
    except requests.RequestException:
        logger.error('Could not connect to {url}'.format(url=url))
        raise ConnectionError
    try:
        requested.raise_for_status()
    except requests.HTTPError as http_error:
        logger.error(http_error)
        raise ConnectionError

    return requested
