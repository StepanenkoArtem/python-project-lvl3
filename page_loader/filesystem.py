# coding=utf-8

"""This module provides file operations."""

import logging
import os

logger = logging.getLogger(__name__)

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
    logger.debug('Try create dir {path}'.format(path=dir_path))
    if not os.path.exists(dir_path):
        logger.info(
            'Create folder for downloading documents on {path}'.format(
                path=dir_path,
            ),
        )
        try:
            os.makedirs(dir_path)
        except PermissionError:
            logger.error(
                'Cannot create directory {dir}. Permission denied'.format(
                    dir=dir_path,
                ),
            )
            raise
        logger.info(
            'Folder {path} successfully created'.format(
                path=dir_path,
            ),
        )


def save_document(document_content, filepath):
    """
    Save document content to file.

    Args:
        document_content (class 'bytes'): Content of html document.
        filepath (str) : Full path to destination file.

    Raises:
        file_not_found (FileNotFoundError) : raise if file not found error
        perm_error (PermissionError) : raise if permission denied
    """
    logger.info('Save document to {path}'.format(path=filepath))
    try:
        with open(filepath, mode=MODE) as document:
            document.write(document_content)
    except FileNotFoundError as file_not_found:
        logger.error(file_not_found)
        raise
    except PermissionError as perm_error:
        logger.error(perm_error)
        raise
