# coding=utf-8

"""This module provides creating 'hyphanated' filenames and paths."""

import logging
import re
from urllib.parse import urlparse

from page_loader import logconf

# Postfixes
_DOC_EXTENSION = '.html'
_RES_DIR_POSTFIX = '_files'

# REGEX Patterns
_HYPHENATE_PATTERN = r'[^0-9a-zA-Z]'
_FILE_EXTENSION = r'(?=\.)[^/]*?$'

_HYPHEN = '-'
_LEADING_SLASH = '/'

logger = logging.getLogger(__name__)


def _hyphenate(path):
    """
    Replace non-alphanumerical symbols to hyphen.

    Args :
        path : str

    Returns :
        str : String with replaced non-alphanumecric symbols
    """
    logger.debug(logconf.DEB_HYPH_HYPHENATE.format(path=path))
    return re.sub(_HYPHENATE_PATTERN, _HYPHEN, path).strip(_HYPHEN)


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
    logger.debug(logconf.DEB_HYPH_TRIM_EXT.format(path=path))
    return re.sub(_FILE_EXTENSION, '', path)


def make_resource_dir_name(document_url):
    """
    Create name for directory where resource files will be saved.

    Add '_files' postfix to 'hyphenated' filename

    Args :
        document_url (str): URL of downloaded document

    Returns :
        str : String contains directory name with '_files' ending.
    """
    prepared_path = '{host}{path}'.format(
        host=urlparse(document_url).netloc,
        path=_trim_extension(urlparse(document_url).path),
    )
    logger.debug(logconf.DEB_HYPH_MAKE_DIR.format(url=document_url))
    return _hyphenate(prepared_path) + _RES_DIR_POSTFIX


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
        logger.debug(logconf.DEB_HYPH_EXT_NOT_EXIST)
        extension = ''
    logger.debug(
        logconf.DEB_HYPH_MAKE_RES_FILENAME.format(path=resource_path),
    )
    return '{base_path}{ext}'.format(
        base_path=_hyphenate(_trim_extension(resource_path)).strip('-'),
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
    basename = '{host}{path}'.format(
        host=urlparse(document_url).netloc,
        path=_trim_extension(urlparse(document_url).path),
    )
    logger.debug(logconf.DEB_HYPH_FILENAME)
    return '{basename}{ext}'.format(
        basename=_hyphenate(basename),
        ext=_DOC_EXTENSION,
    )
