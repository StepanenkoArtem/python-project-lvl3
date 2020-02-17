import json

from page_loader.validate_args import _validate_path  # noqa: WPS436
from page_loader.validate_args import _validate_url  # noqa: WPS436


def test_validate_url():
    fixtures = 'tests/fixtures/validate/urls.json'
    with open(fixtures) as expected_data:
        urls = json.load(expected_data)
        for url, expected in urls.items():
            assert expected == _validate_url(url)


def test_validate_path():
    fixtures = 'tests/fixtures/validate/paths.json'
    with open(fixtures) as expected_data:
        paths = json.load(expected_data)
        for path, expected in paths.items():
            assert expected == _validate_path(path)
