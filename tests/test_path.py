# coding=utf-8

"""Check replacing non-alphanumeric symbols to dash in paths."""

import json

import pytest
from loader import path


def dataset(dataset_file):
    """Get testing data from dataset file.

    Args:
        dataset_file : path to file with JSON dataset

    Returns:
        : dictionary contains {expected: origin}
    """
    return json.loads(open(dataset_file).read()).items()


@pytest.mark.parametrize(
    'resource_path, expected_dir_name',
    dataset('tests/datasets/path/for_resource_dir.json'),
)
def test_for_resource_dir(resource_path, expected_dir_name):
    """
    Check replacing non-alphanumeric symbols in resource directory name.

    Args:
        resource_path (str) : origin path.
        expected_dir_name (str) : expected modified directory name.
    """
    # CHECK
    assert expected_dir_name == path.for_resource_dir(
        resource_path,
    )


@pytest.mark.parametrize(
    'resource_path, expected_filename',
    dataset('tests/datasets/path/for_resource.json'),
)
def test_for_resource(resource_path, expected_filename):
    """
    Check replacing non-alphanumeric symbols in filename.

    Args:
        resource_path (str) : origin filename path
        expected_filename (str) : modified ("dashed") filename
    """
    # CHECK
    assert expected_filename == path.for_resource(resource_path)


@pytest.mark.parametrize(
    'document_path, expected_filename',
    dataset('tests/datasets/path/for_page.json'),
)
def test_for_page(document_path, expected_filename):
    """
    Check replacing non-aplhanumeric symbols in document path name.

    Args:
        document_path (str) : origin document path
        expected_filename (str) : expected modified filepath
    """
    # CHECK
    assert expected_filename == path.for_page(
        document_path,
    )
