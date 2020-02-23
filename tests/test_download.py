from page_loader.download import clean_url, get_requested
from tests.get_data import get_data_from_json


def test_clean_url():
    expected = get_data_from_json(
        'tests/data/download/clean_url.json',
    )
    for url, cleaned_url in expected.items():
        assert clean_url(url) == cleaned_url


def test_download():
    expected = get_data_from_json('tests/data/download/urls.json')
    for url, status_code in expected.items():
        assert get_requested(url).status_code == status_code
