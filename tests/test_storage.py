# coding=utf-8

import os

import pytest
from loader import storage

PERMS = 0x111
READ_ONLY_DIR = 'read_only_dir'
TEST_DIR = 'test_dir'
TEST_FILE = 'testfile.txt'


@pytest.fixture
def get_fake_content():
    with open('tests/datasets/filesystem/html_doc.gold', 'rb') as golden:
        return golden.read()


def test_create_dir_exceptions(tmpdir):
    os.mkdir(os.path.join(tmpdir, READ_ONLY_DIR), mode=PERMS)
    full_dir_path = os.path.join(tmpdir, READ_ONLY_DIR, 'sub_dir')
    with pytest.raises(PermissionError):
        assert storage.create_dir(full_dir_path)


def test_save(get_fake_content, tmpdir):
    filepath = os.path.join(tmpdir, TEST_FILE)
    storage.save(get_fake_content, filepath)
    with open(filepath, 'rb') as expected:
        assert get_fake_content == expected.read()


def test_save_exceptions(get_fake_content, tmpdir):
    # Test raises PermissionError
    os.mkdir(os.path.join(tmpdir, READ_ONLY_DIR), mode=PERMS)
    filepath = os.path.join(tmpdir, READ_ONLY_DIR, TEST_FILE)
    with pytest.raises(PermissionError):
        assert storage.save(get_fake_content, filepath)
