from page_loader.download import _clean_url, download
from tests.get_data import get_data_from_json


def test_clean_url():
    expected = get_data_from_json(
        'tests/data/download/clean_url.json',
    )
    for url, cleaned_url in expected.items():
        assert _clean_url(url) == cleaned_url


def test_download():
    expected = get_data_from_json('tests/data/download/urls.json')
    for url, status_code in expected.items():
        assert download(url).status_code == status_code
