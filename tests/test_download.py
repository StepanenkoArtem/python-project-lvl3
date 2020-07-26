# coding=utf-8

import pytest
from page_loader import download


def test_downloads():
    """Testing download() returns value."""  # noqa: DAR201
    expected = ''
    actual = download.download()
    assert actual == expected


def test_downloads_excetions():
    """Testing download() exceptions."""  # noqa: DAR201
    with pytest.raises(ConnectionError):
        assert download.download()
