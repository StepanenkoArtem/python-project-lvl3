from page_loader.save import _make_filename_from_url, save_requsted  # noqa: WPS436
from tests.get_fixtures import get_fixture_from_json


def test_set_name():
    filenames = get_fixture_from_json(
        'tests/fixtures/save/uri_to_filename.json',
    )
    for url, expected in filenames.items():
        assert _make_filename_from_url(url) == expected


#def test_save_requested():
 #   save_requsted()
