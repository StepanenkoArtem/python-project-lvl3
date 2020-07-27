# coding=utf-8

"""This module provides file operations."""

import logging
import os

from page_loader import settings

logger = logging.getLogger(__name__)
# File operation mode
MODE = 'wb'


def create_dir(dir_path):
    """
    Create destination directory.

    Args:
        dir_path : str
            Path for directory

    Returns:
        (str): Returns path if directory created successfully

    Raises:
        PermissionError : if cannot create subfolder
    """
    if not os.path.exists(dir_path):
        logger.debug(settings.DEB_FS_CREATE_DIR)
        try:
            os.makedirs(dir_path)
        except PermissionError:
            logger.error(settings.ERR_FS_PERMISSION_DND)
            raise
    return dir_path


def save_document(document_content, filepath):
    """
    Save document content to file.

    Args:
        document_content (class 'bytes'): Content of html document.
        filepath (str) : Full path to destination file.

    Raises:
        FileNotFoundError : raise if file not found error
        PermissionError : raise if permission denied
    """
    try:
        with open(filepath, mode=MODE) as document:
            document.write(document_content)
    except FileNotFoundError:
        logger.error(settings.ERR_FS_CREATE_FILE_ERR)
        raise
    except PermissionError:
        logger.error(settings.ERR_FS_PERMISSION_DND)
        raise
