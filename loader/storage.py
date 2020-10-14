# coding=utf-8

"""This module provides file operations."""

import os

# File operation mode
MODE = 'wb'


def create_dir(dir_path):
    """
    Create destination directory.

    Args:
        dir_path : str
            Path for directory

    Raises:
        PermissionError : if cannot create subfolder
    """
    dir_path = os.path.normpath(dir_path)

    if not os.path.exists(dir_path):
        try:
            os.makedirs(dir_path)
        except PermissionError:
            raise


def save(document_content, filepath):
    """
    Save document content to file.

    Args:
        document_content (class 'bytes'): Content of html document.
        filepath (str) : Full path to destination file.

    Raises:
        file_not_found (FileNotFoundError) : raise if file not found error
        perm_error (PermissionError) : raise if permission denied
    """
    try:
        with open(filepath, mode=MODE) as document:
            document.write(document_content)
    except FileNotFoundError as file_not_found:
        raise FileNotFoundError from file_not_found
    except PermissionError as perm_error:
        raise PermissionError from perm_error
