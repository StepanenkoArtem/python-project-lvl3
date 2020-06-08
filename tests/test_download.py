import pytest
from page_loader import download
from tests.fixtures.get_dataset_from_file import get_dataset_from_file

_DS_URL_NORMALIZE = 'tests/datasets/download/url_norm.json'


@pytest.mark.parametrize(
    'url, normalized', get_dataset_from_file(_DS_URL_NORMALIZE),
)
def test_url_normalize(url, normalized):
    assert normalized == download.url_normalize(url)
