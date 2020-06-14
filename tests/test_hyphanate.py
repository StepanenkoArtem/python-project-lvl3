from page_loader import hyphenate
from tests.fixtures.get_dataset_from_file import get_dataset_from_json

_DS_MAKE_RES_DIR_NAME = \
    'tests/datasets/hyphenate/test_make_resource_dir_name.json'
_DS_MAKE_RES_FILENAME = \
    'tests/datasets/hyphenate/test_make_resource_filename.json'
_DS_MAKE_DOCUMENT_NAME = \
    'tests/datasets/hyphenate/test_make_document_name.json'


def test_make_resource_dir_name():  # noqa: D103
    test_data = get_dataset_from_json(_DS_MAKE_RES_DIR_NAME)
    for resource_path, expected_dir_name in test_data:
        assert expected_dir_name == hyphenate.make_resource_dir_name(
            resource_path,
        )


def test_make_resource_filename():  # noqa: D103
    test_data = get_dataset_from_json(_DS_MAKE_RES_FILENAME)
    for resource_path, expected_filename in test_data:
        assert expected_filename == hyphenate.make_resource_filename(
            resource_path,
        )


def test_make_document_name():  # noqa: D103
    test_data = get_dataset_from_json(_DS_MAKE_DOCUMENT_NAME)
    for document_path, expected_filename in test_data:
        assert expected_filename == hyphenate.make_document_name(
            document_path,
        )
