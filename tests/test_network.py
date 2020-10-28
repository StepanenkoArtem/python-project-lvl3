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


@pytest.mark.xfail
def test_redirects():
    """Testing 3xx response."""
    with pytest.raises(network.NetworkError):
        network.download('https://httpbin.org/status/301')
        network.download('https://httpbin.org/status/302')
        network.download('https://httpbin.org/status/201')


def test_client_connection_errors():
    """Testing 4xx Error exceptions."""
    with pytest.raises(network.NetworkError):
        network.download('https://httpbin.org/status/404')
        network.download('https://httpbin.org/status/403')


def test_server_connection_errors():
    """Testing 5xx Error exceptions."""
    with pytest.raises(network.NetworkError):
        network.download('https://httpbin.org/status/500')
        network.download('https://httpbin.org/status/502')


def test_network_failed_connection():
    """Testing failed connection exceptions."""
    with pytest.raises(network.NetworkError):
        network.download('https://#incetorrectdomain.com')
        network.download('')
