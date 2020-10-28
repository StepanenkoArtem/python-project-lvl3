# coding=utf-8

"""Check replacing non-alphanumeric symbols to dash in paths."""

import json

import pytest
from loader import path


@pytest.mark.parametrize(
    'resource_path, expected_dir_name',
    json.load(
        open('tests/datasets/path/for_resource_dir.json'),
    ).items(),
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
    json.load(
        open('tests/datasets/path/for_resource.json'),
    ).items(),
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
    json.load(
        open('tests/datasets/path/for_page.json'),
    ).items(),
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
