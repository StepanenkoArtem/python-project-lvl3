# coding=utf-8

"""Retrive URL resource."""

import logging

import requests
from page_loader import logconf, settings
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
    logger.debug(logconf.DEB_DL_URL_GET.format(url=url))
    try:
        requested = requests.get(
            url=url_normalize(url),
            timeout=settings.DEFAULT_TIMEOUT,
        )
    except (
        requests.RequestException,
        requests.ReadTimeout,
    ) as request_error:
        logger.error(request_error)
        raise ConnectionError

    try:
        requested.raise_for_status()
    except requests.HTTPError as http_error:
        logger.error(http_error)
        raise ConnectionError

    return requested
