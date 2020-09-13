# coding=utf-8

import pytest
from page_loader import download

STATUS_OK = 200


def test_downloads_success():
    """Testing download() returns value."""
    actual = download.download('https://httpbin.org/status/200')
    assert actual.status_code == STATUS_OK


def test_downloads_exceptions():
    """Testing download() exceptions."""
    with pytest.raises(ConnectionError):
        assert download.download('https://httpbin.org/status/404')
    with pytest.raises(ConnectionError):
        assert download.download('https://fgsdfgsdfgsd.com')
    with pytest.raises(ConnectionError):
        assert download.download('')
