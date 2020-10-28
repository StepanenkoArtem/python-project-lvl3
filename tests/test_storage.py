# coding=utf-8

"""Test filesystem operations."""

import os

import pytest
from loader import storage

READ_ONLY = 0x111
RO_DIR = 'ro_dir'
TEST_DIR = 'test_dir'
TEST_FILE = 'testfile.txt'


@pytest.fixture
def testing_content():
    """Get test content from file.

    Returns:
        : file contents in bytes
    """
    return open('tests/datasets/storage/test.html', 'rb').read()


def test_create_dir_exceptions(tmpdir):
    """Check raising exceptions if permission error occured.

    Args:
        tmpdir: temporary base directory
    """
    # PREPARE
    # Set read-only permissions to tmpdir
    os.chmod(tmpdir, READ_ONLY)

    # Make fullpath for test directory
    test_dir = os.path.join(tmpdir, TEST_DIR)

    # CHECK
    with pytest.raises(storage.StorageError):
        storage.mkdir(test_dir)


def test_save(testing_content, tmpdir):
    """Check is saved content is equal to test content.

    Args:
        testing_content : bytes was gotten from file
        tmpdir : temporary directory
    """
    # PREPARE
    # EXCERSIZE
    storage.save(testing_content, tmpdir, TEST_FILE)
    # CHECK
    expected = open(os.path.join(tmpdir, TEST_FILE), 'rb')
    assert testing_content == expected.read()


def test_save_exceptions(testing_content, tmpdir):
    """Check raising Exception if file storage error occured.

    Args:
        testing_content : bytes was gotten from file
        tmpdir : temporary_directory
    """
    # SETUP
    # Create temporary dir with read-only permissions
    os.chmod(tmpdir, mode=READ_ONLY)

    # EXCERSIZE
    with pytest.raises(storage.StorageError):
        storage.save(
            f_content=testing_content,
            output=tmpdir,
            filename=TEST_FILE,
        )
