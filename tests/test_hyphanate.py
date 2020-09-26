# coding=utf-8

"""Check replacing non-alphanumeric symbols to dash in paths."""

import json

import pytest
from page_loader import hyphenate


@pytest.mark.parametrize(
    'resource_path, expected_dir_name',
    json.load(
        open('tests/datasets/hyphenate/test_make_resource_dir_name.json'),
    ).items(),
)
def test_make_resource_dir_name(resource_path, expected_dir_name):
    """
    Check replacing non-alphanumeric symbols in resource directory name.

    Args:
        resource_path (str) : origin path.
        expected_dir_name (str) : expected modified directory name.
    """
    assert expected_dir_name == hyphenate.make_resource_dir_name(
        resource_path,
    )


@pytest.mark.parametrize(
    'resource_path, expected_filename',
    json.load(
        open('tests/datasets/hyphenate/test_make_resource_filename.json'),
    ).items(),
)
def test_make_resource_filename(resource_path, expected_filename):
    """
    Check replacing non-alphanumeric symbols in filename.

    Args:
        resource_path (str) : origin filename path
        expected_filename (str) : modified ("dashed") filename
    """
    assert expected_filename == hyphenate.make_resource_filename(
        resource_path,
    )


@pytest.mark.parametrize(
    'document_path, expected_filename',
    json.load(
        open('tests/datasets/hyphenate/test_make_document_name.json'),
    ).items(),
)
def test_make_document_name(document_path, expected_filename):
    """
    Check replacing non-aplhanumeric symbols in document path name.

    Args:
        document_path (str) : origin document path
        expected_filename (str) : expected modified filepath
    """
    assert expected_filename == hyphenate.make_document_name(
        document_path,
    )
