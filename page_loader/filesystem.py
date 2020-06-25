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

    Returns:
        (str | Boolean): Returns path if directory created successfully,
        esle returns False

    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path


def save_document(document_content, path_file):
    """
    Save document content to file.

    Args:
        document_content (class 'bytes'): Content of html document.
        path_file (str) : Full path to destination file.

    """
    with open(path_file, mode=MODE) as document:
        document.write(document_content)
