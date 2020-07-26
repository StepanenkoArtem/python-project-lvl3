# coding=utf-8

import pytest
from page_loader import download


def test_downloads():
    """Testing download() returns value."""  # noqa: DAR201
    expected = ''
    actual = download.download('https://httpbin.org/status/200')
    assert actual == expected


def test_downloads_exceptions():
    """Testing download() exceptions."""  # noqa: DAR201
    with pytest.raises(ConnectionError):
        assert download.download('https://httpbin.org/status/404')

    with pytest.raises(ConnectionError):
        assert download.download('https://baklazhan.com.ua')

    with pytest.raises(ConnectionError):
        assert download.download('https://httpfdfdbin.org/stafdftus/404')
