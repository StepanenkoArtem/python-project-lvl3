import json
from page_loader.validate_args import _validate_path, _validate_url


def test_validate_url():
    fixtures = 'tests/fixtures/urls.json'
    paths = json.load(open(fixtures))
    for path, value in paths.items():
        assert value == _validate_url(path)


def test_validate_path():
    fixtures = 'tests/fixtures/paths.json'
    paths = json.load(open(fixtures))
    for path, value in paths.items():
        assert value == _validate_path(path)
