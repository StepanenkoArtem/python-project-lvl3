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
    """
    logger.warning('start download URL={url}'.format(url=url))
    downloaded = requests.get(url_normalize(url))
    if downloaded.status_code == settings.STATUS_OK:
        return downloaded
    return None
