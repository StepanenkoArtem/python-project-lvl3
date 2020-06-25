# coding=utf-8

"""This module provides creating 'hyphanated' filenames and paths."""

import re

# Postfixes
_DOC_EXTENSION = '.html'
_RES_DIR_POSTFIX = '_files'

# REGEX Patterns
_HYPHENATE_PATTERN = r'[^0-9a-zA-Z]'
_FILE_EXTENSION = r'(?=\.)[^/]*?$'

_HYPHEN = '-'
_LEADING_SLASH = '/'


def _hyphenate(path):
    """
    Replace non-alphanumerical symbols to hyphen.

    Args :
        path : str

    Returns :
        str : String with replaced non-alphanumecric symbols
    """
    return re.sub(_HYPHENATE_PATTERN, _HYPHEN, path)


def _trim_extension(path):
    """
    Get resource file basename without file extendion.

    Args :
        path:
            path to local resource fils

    Returns:
        str: string
            resource file basenamr.
    """
    return re.sub(_FILE_EXTENSION, '', path.strip(_LEADING_SLASH))


def make_resource_dir_name(document_path):
    """
    Create name for directory where resource files will be saved.

    Add '_files' postfix to 'hyphenated' filename

    Args :
        document_path (str): URL of downloaded document

    Returns :
        str : String contains directory name with '_files' ending.
    """
    return '{file_basename}{ext}'.format(
        file_basename=_hyphenate(_trim_extension(document_path)),
        ext=_RES_DIR_POSTFIX,
    )


def make_resource_filename(resource_path):
    """
    Create filename for resource file.

    Args :
        resource_path : str
            Contains path to resource files obtained from html document.

    Returns :
        str : Filename with replaced non-alpanumerical symbols
        and original filextension.
    """
    try:
        extension = re.search(_FILE_EXTENSION, resource_path).group(0)
    except AttributeError:
        extension = ''
    return '{base_path}{ext}'.format(
        base_path=_hyphenate(_trim_extension(resource_path)),
        ext=extension,
    )


def make_document_name(document_url):
    """
    Create hypheneted filename for downloaded document.

    Args :
        document_url (str) : document url

    Returns :
        str : Filename with replaced non-alphanumerical symbols
        and with 'html' - extendion
    """
    return '{file_basename}{ext}'.format(
        file_basename=_hyphenate(
            _trim_extension(document_url),
        ),
        ext=_DOC_EXTENSION,
    )
