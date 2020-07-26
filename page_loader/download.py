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
        ConnectionError : Cantnot establish connection to host
    """
    logger.debug(settings.DEB_DL_URL_GET.format(url=url))
    try:
        return requests.get(url_normalize(url))
    except requests.ConnectionError:
        logger.error(settings.ERR_DL_CONNECTTION.format(url=url))
        raise ConnectionError
    except TimeoutError:
        logger.error(settings.ERR_DL_CONNECTTION.format(url=url))
        raise ConnectionError
