from unittest.mock import Mock

import pytest
from page_loader import localize
from tests.fixtures.get_dataset_from_file import get_dataset_from_file

_DS_IS_LOCAL = 'tests/datasets/localize/is_local.json'
_DS_GET_RESOURCE_HOST = 'tests/datasets/localize/get_resource_host.json'
_DS_GET_RESOURCE_PATH = 'tests/datasets/localize/get_resource_path.json'
_DS_UPDATE_RESOURCE_FILENAME = 'tests/datasets/localize/update_resource_filename.json'  # noqa: E501


@pytest.mark.parametrize(
    'path, expected', get_dataset_from_file(_DS_IS_LOCAL),
)
def test_is_local(path, expected):
    resource = Mock()
    resource.path = Mock()
    resource.get = Mock(return_value=path)
    assert expected == localize._is_local(resource)  # noqa: WPS437


@pytest.mark.parametrize(
    'url, host',
    get_dataset_from_file(_DS_GET_RESOURCE_HOST),
)
def test_get_resource_host(url, host):
    assert host == localize.get_resource_host(url)


@pytest.mark.parametrize(
    'url, path', get_dataset_from_file(_DS_GET_RESOURCE_PATH),
)
def test_get_resource_path(url, path):
    resource = Mock()
    resource.path = Mock()
    resource.get = Mock(return_value=path)
    assert path == localize.get_resource_path(resource)


@pytest.mark.parametrize(
    'path, filename',
    get_dataset_from_file(_DS_UPDATE_RESOURCE_FILENAME),
)
def test_update_resource_filename(path, filename):
    assert filename == localize.set_local_resource_filename(path)
