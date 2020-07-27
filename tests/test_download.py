# coding=utf-8

import pytest
from page_loader import download


def test_downloads_success():
    """Testing download() returns value."""  # noqa: DAR201
    test_url = 'https://httpbin.org/status/200'
    actual = download.download(test_url)
    expected = 200
    assert actual.status_code == expected


def test_downloads_exceptions():
    """Testing download() exceptions."""  # noqa: DAR201
    with pytest.raises(ConnectionError):
        assert download.download('https://httpbin.org/status/404')
    with pytest.raises(ConnectionError):
        assert download.download('https://fgsdfgsdfgsd.com')
    with pytest.raises(ConnectionError):
        assert download.download('')
