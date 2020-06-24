# coding=utf-8

"""This module provides file operations."""

import os

# File operation modes
WRITE_B = 'wb'


def create_dir(output):
    """
    Create destination directory.

    Args:
        output : str
            Path for directory

    Returns:
        (str | Boolean): Returns path if directory created successfully,
        esle returns False

    """
    if not os.path.exists(output):
        os.makedirs(output)
        return (output)
    return False


def save_document(document_content, path_file):
    """
    Save document content to file.

    Args:
        document_content (class 'bytes'): Content of html document.
        path_file (str) : Full path to destination file.

    """
    with open(path_file, mode=WRITE_B) as document:
        document.write(document_content)
