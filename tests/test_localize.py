import json
from unittest.mock import Mock

from page_loader.localize import _is_local


def test_is_local():
    resource = Mock()
    with open('tests/fixtures/is_local.json') as test_data_file:
        test_data = json.load(test_data_file)
    for path, expected in test_data.items():
        resource.path = Mock()
        resource.get = Mock(return_value=path)
        assert expected == _is_local(resource)


def test_get_resource_url():
    return None


def test_get_resource_path():
    return None


def test_set_local_resource_filename():
    return None
