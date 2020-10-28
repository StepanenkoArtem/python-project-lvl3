# coding=utf-8

"""This module provides creating 'hyphanated' filenames and paths."""

import os
import re
from urllib.parse import urlparse

# REGEX Patterns
HYPHENATE_PATTERN = re.compile(r'[^0-9a-zA-Z]')


def hyphenate(path):
    """
    Replace non-alphanumerical symbols to hyphen.

    Args :
        path : str

    Returns :
        str : String with replaced non-alphanumecric symbols
    """
    return re.sub(HYPHENATE_PATTERN, '-', path).strip('-')


def prepare_basename(document_url):
    """Prepare basename from document URL.

    Args :
        document_url (str): URL of downloaded document

    Returns :
        str : Basename
    """
    host = urlparse(document_url).netloc
    path, _ = os.path.splitext(urlparse(document_url).path)
    return host + path


def for_resource_dir(document_url):
    """
    Create name for directory where resource files will be saved.

    Add '_files' postfix to basename

    Args :
        document_url (str): URL of downloaded document

    Returns :
        str : String contains directory name with '_files' postfix.
    """
    basename = prepare_basename(document_url)
    return hyphenate(basename) + '_files'


def for_resource(resource_path):
    """
    Create filename for resource file.

    Args :
        resource_path : str
            Contains path to resource files obtained from html document.

    Returns :
        str : Filename with replaced non-alpanumerical symbols
        and original filextension.
    """
    path, extension = os.path.splitext(resource_path)
    return hyphenate(path) + extension


def for_page(document_url):
    """
    Create filename for downloaded document.

    Args :
        document_url (str) : document url

    Returns :
        str : Filename with replaced non-alphanumerical symbols
        and with 'html' - extendion
    """
    basename = prepare_basename(document_url)
    return hyphenate(basename) + '.html'
