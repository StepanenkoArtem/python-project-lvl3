from unittest.mock import MagicMock, Mock

from page_loader import localize
from tests.fixtures.get_dataset_from_file import get_dataset_from_json

_DS_IS_LOCAL = 'tests/datasets/localize/is_local.json'
_DS_GET_DOCUMENT_HOST = 'tests/datasets/localize/get_document_host.json'
_DS_GET_RESOURCE_PATH = 'tests/datasets/localize/get_resource_path.json'
_DS_UPDATE_RESOURCE_FILENAME = 'tests/datasets/localize/update_resource_filename.json'  # noqa: E501
_DS_URL_NORMALIZE = 'tests/datasets/localize/url_norm.json'
_DS_SET_RESOURCE_LINK = 'tests/datasets/localize/set_new_link.json'


def test_url_normalize():  # noqa: D103
    for url, normalized in get_dataset_from_json(_DS_URL_NORMALIZE):
        assert normalized == localize.url_normalize(url)


def test_is_local():  # noqa: D103
    for path, expected in get_dataset_from_json(_DS_IS_LOCAL):
        resource = Mock()
        resource.path = Mock()
        resource.get = Mock(return_value=path)
        assert expected == localize._is_local(resource)  # noqa: WPS437


def test_get_resource_path():  # noqa: D103
    for url, path in get_dataset_from_json(_DS_GET_RESOURCE_PATH):
        resource = Mock()
        resource.path = Mock()
        resource.get = Mock(return_value=url)
        assert path == localize.get_resource_path(resource)


def test_set_new_link_on_doc():  # noqa: D103
    old_resource = MagicMock()
    old_resource.attrs = {'href': 'old_value'}

    new_resource = MagicMock()
    new_resource.attrs = {'href': 'new_link'}

    expected = new_resource.attrs
    actual = localize.set_new_resource_link_on_doc(old_resource, 'new_link').attrs

    assert expected == actual
