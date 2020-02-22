from page_loader.save import make_filename_from_url
from tests.get_fixtures import get_fixture_from_json


def test_make_filename_from_url():
    filenames = get_fixture_from_json(
        'tests/data/save/uri_to_filename.json',
    )
    for url, expected in filenames.items():
        assert make_filename_from_url(url) == expected
