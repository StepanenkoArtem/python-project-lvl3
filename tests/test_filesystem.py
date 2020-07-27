# coding=utf-8

import os

import pytest
from page_loader.filesystem import create_dir, save_document

PERMS = 111
READ_ONLY_DIR = 'read_only_dir'
TEST_DIR = 'test_dir'
TEST_FILE = 'testfile.txt'


def test_create_dir(fs):  # noqa: D103
    test_dir = 'test_dir'
    create_dir(test_dir)
    assert os.path.exists(test_dir)


def test_create_dir_on_readonly_dir(fs):  # noqa: D103
    fs.create_dir(READ_ONLY_DIR, perm_bits=PERMS)
    full_dir_path = os.path.join(READ_ONLY_DIR, 'sub_dir')
    with pytest.raises(PermissionError):
        assert create_dir(full_dir_path)


@pytest.fixture
def get_fake_content():  # noqa: D103
    with open('tests/datasets/filesystem/html_doc.gold', 'rb') as golden:
        return golden.read()


def test_save_document(get_fake_content, fs, tmpdir):  # noqa: D103
    filepath = tmpdir.mkdir(TEST_DIR).join(TEST_FILE)
    save_document(get_fake_content, filepath)
    with open(filepath, 'rb') as expected:
        assert get_fake_content == expected.read()


def test_save_document_perm_error(get_fake_content, fs):  # noqa: D103
    fs.create_dir(READ_ONLY_DIR, perm_bits=PERMS)
    filepath = os.path.join(READ_ONLY_DIR, TEST_FILE)
    with pytest.raises(PermissionError):
        assert save_document(get_fake_content, filepath)


def test_save_document_not_found_error(get_fake_content, fs):  # noqa: D103
    fs.create_dir(READ_ONLY_DIR)
    filepath = os.path.join(TEST_DIR, TEST_FILE)
    with pytest.raises(FileNotFoundError):
        assert save_document(get_fake_content, filepath)
