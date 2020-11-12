# coding=utf-8

"""Test working with net."""

import pytest
from loader import network


def test_download():
    """Test downloading URL document."""
    # PREPARE
    expected = open(
        'tests/pages/origin/stepanenkoartem.github.io.html',
        mode='rb',
    ).read()
    actual = network.download('https://stepanenkoartem.github.io/')
    # CHECK
    assert expected == actual


@pytest.mark.parametrize(
    'url',
    [
        'https://httpbin.org/status/301',
        'https://httpbin.org/status/302',
    ],
)
@pytest.mark.xfail
def test_redirects(url):
    """Testing 3xx response.

    Args:
        url : (str) test URL
    """
    with pytest.raises(network.NetworkError):
        network.download(url)


@pytest.mark.parametrize(
    'url',
    [
        'https://httpbin.org/status/403',
        'https://httpbin.org/status/404',
    ],
)
def test_client_connection_errors(url):
    """Testing 4xx Error exceptions.

    Args:
        url : (str) test URL
    """
    with pytest.raises(network.NetworkError):
        network.download(url)


@pytest.mark.parametrize(
    'url',
    [
        'https://httpbin.org/status/500',
        'https://httpbin.org/status/502',
    ],
)
def test_server_connection_errors(url):
    """Testing 5xx Error exceptions.

    Args:
        url : (str) test URL
    """
    with pytest.raises(network.NetworkError):
        network.download(url)


@pytest.mark.parametrize(
    'url',
    [
        'https://#incetorrectdomain.com',
        ' ',
    ],
)
def test_network_failed_connection(url):
    """Testing failed connection exceptions.

    Args:
        url : (str) test URL
    """
    with pytest.raises(network.NetworkError):
        network.download(url)
