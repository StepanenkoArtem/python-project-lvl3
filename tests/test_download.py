# coding=utf-8

import pytest
from page_loader.download import get_page


def test_downloads_exceptions():
    """Testing download() exceptions."""
    with pytest.raises(ConnectionError):
        assert get_page('https://httpbin.org/status/404')
    with pytest.raises(ConnectionError):
        assert get_page('https://#incetorrectdomain.com')
    with pytest.raises(ConnectionError):
        assert get_page('')
