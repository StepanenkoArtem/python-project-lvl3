# coding=utf-8

import os

import pytest
from page_loader.filesystem import create_dir, save_document

PERMS = 0x111
READ_ONLY_DIR = 'read_only_dir'
TEST_DIR = 'test_dir'
TEST_FILE = 'testfile.txt'


def test_create_dir_on_readonly_dir(tmpdir):  # noqa: D103
    os.mkdir(os.path.join(tmpdir, READ_ONLY_DIR), mode=PERMS)
    full_dir_path = os.path.join(tmpdir, READ_ONLY_DIR, 'sub_dir')
    with pytest.raises(PermissionError):
        assert create_dir(full_dir_path)


@pytest.fixture
def get_fake_content():
    with open('tests/datasets/filesystem/html_doc.gold', 'rb') as golden:
        return golden.read()


def test_save_document(get_fake_content, tmpdir):
    filepath = os.path.join(tmpdir, TEST_FILE)
    save_document(get_fake_content, filepath)
    with open(filepath, 'rb') as expected:
        assert get_fake_content == expected.read()


def test_save_document_perm_error(get_fake_content, tmpdir):
    os.mkdir(os.path.join(tmpdir, READ_ONLY_DIR), mode=PERMS)
    filepath = os.path.join(tmpdir, READ_ONLY_DIR, TEST_FILE)
    with pytest.raises(PermissionError):
        assert save_document(get_fake_content, filepath)


def test_save_document_not_found_error(get_fake_content, tmpdir):
    os.mkdir(os.path.join(tmpdir, READ_ONLY_DIR))
    filepath = os.path.join(tmpdir, TEST_DIR, TEST_FILE)
    with pytest.raises(FileNotFoundError):
        assert save_document(get_fake_content, filepath)
