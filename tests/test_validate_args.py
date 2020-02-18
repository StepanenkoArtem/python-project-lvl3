import json
from tests.get_fixtures import get_fixture_from_json
from page_loader.validate_args import _validate_path  # noqa: WPS436
from page_loader.validate_args import _validate_url  # noqa: WPS436


def test_validate_url():
    urls = get_fixture_from_json('tests/fixtures/validate/urls.json')
    for url, expected in urls.items():
        assert expected == _validate_url(url)


def test_validate_path():
    paths = get_fixture_from_json('tests/fixtures/validate/paths.json')
    for path, expected in paths.items():
        assert expected == _validate_path(path)
