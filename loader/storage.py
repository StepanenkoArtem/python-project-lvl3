# coding=utf-8

"""This module provides file operations."""

import os


class StorageError(Exception):
    """Define StorageError Exceptions."""

    def __init__(self, message):
        """Init Storage Exception.

        Args:
            message: str
                Exception's message
        """
        self.exit_code = 2
        self.message = message

    def __str__(self):
        """Show user friendly-message.

        Returns:
            message : (str)
        """
        return self.message


def mkdir(dir_path):
    """
    Create destination directory.

    Args:
        dir_path : str
            Path for directory

    Raises:
        StorageError : Raise if cannot create subfolder
    """
    try:
        os.makedirs(dir_path)
    except FileExistsError as file_exist_error:
        raise StorageError(
            message='Directory {dir} already exist'.format(dir=dir_path),
        ) from file_exist_error
    except PermissionError as perm_error:
        raise StorageError(
            message="Can't creat dir {dir}. Permission denied.".format(
                dir=dir_path,
            ),
        ) from perm_error


def save(f_content, output, filename):
    """
    Save content to file.

    Args:
        f_content : (bytes) HTML content in bytes.
        filename : (str)
        output : (str) destination dir to save file

    Raises:
        StorageError : raise if file storage error occured
    """
    try:
        with open(
            os.path.join(output, filename),
            mode='wb',
        ) as document:
            document.write(f_content)
    except (FileNotFoundError, PermissionError) as file_storage_err:
        raise StorageError(
            message='Cannot save file {file}'.format(file=filename),
        ) from file_storage_err
