# coding=utf-8

import os

import pytest
from page_loader.filesystem import create_dir, save_document


def test_create_dir(fs):  # noqa: D103
    test_dir = 'test_dir'
    create_dir(test_dir)
    assert os.path.exists(test_dir)


def test_create_dir_on_readonly_dir(fs):  # noqa: D103
    permissions = 111
    if os.name == 'nt':
        read_only_dir = os.path.join('C:/', 'read_only_dir')
    else:
        read_only_dir = os.path.join('read_only_dir')
    fs.create_dir(read_only_dir, perm_bits=permissions)
    full_path = os.path.join(read_only_dir, 'sub_dir')
    with pytest.raises(PermissionError):
        assert create_dir(full_path)


@pytest.fixture
def get_fake_content():  # noqa: D103
    with open('tests/datasets/filesystem/html_doc.gold', 'rb') as golden:
        return golden.read()


def test_save_document(get_fake_content, fs, tmpdir):  # noqa: D103
    path_file = tmpdir.mkdir('test').join('test_file.txt')
    fake_content = get_fake_content
    save_document(fake_content, path_file)
    with open(path_file, 'rb') as expected:
        assert fake_content == expected.read()
