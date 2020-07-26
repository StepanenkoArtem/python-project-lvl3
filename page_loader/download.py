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
            Url address specified from command-lina args

    Returns:
        downloaded : <requests.object>

    Raises:
        ConnectionError : Cannot establish connection to host
    """
    logger.debug(settings.DEB_DL_URL_GET.format(url=url))
    try:
        requested = requests.get(
            url=url_normalize(url),
            timeout=settings.DEFAULT_TIMEOUT,
        )
    except requests.RequestException as req_error:
        logger.error(req_error)
        raise ConnectionError

    try:
        requested.raise_for_status()
    except requests.RequestException as http_err:
        logger.error(http_err)
        raise ConnectionError

    return requested
