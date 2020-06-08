import os

import pytest
from page_loader.filesystem import create_dir


def test_create_dir(fs):  # noqa: D103
    test_dir = '/home/chief/dir4444'
    create_dir(test_dir)
    assert os.path.exists(test_dir)


def test_create_dir_on_readonly_dir(fs):  # noqa: D103
    permissions = 111
    read_only_dir = 'readonly_dir'
    test_dir = 'some_dir'
    fs.create_dir(read_only_dir, perm_bits=permissions)
    full_path = '{read_only}/{some_dir}'.format(
        read_only=read_only_dir,
        some_dir=test_dir,
    )
    with pytest.raises(PermissionError):
        assert create_dir(full_path)


def test_save_document():  # noqa: D103
    return None
