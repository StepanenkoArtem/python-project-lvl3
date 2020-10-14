# coding=utf-8

"""Retrive URL resource."""

import requests


def get_page(url):
    """
    Download requested url.

    Args:
        url : str
            Url address specified from command-line args

    Returns:
        downloaded : bytes
            Content of downloaded page

    Raises:
        ConnectionError : Cannot establish connection to host
    """
    try:
        requested = requests.get(
            url=url,
            timeout=3,
        )
    except requests.RequestException as failed_request:
        raise ConnectionError from failed_request
    try:
        requested.raise_for_status()
    except requests.HTTPError as http_error:
        raise ConnectionError from http_error

    return requested.content
