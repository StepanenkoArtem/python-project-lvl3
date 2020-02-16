from page_loader.download import get_web_content


def test_download():
    test_url = 'hexlet'
    assert get_web_content(test_url) == test_url
