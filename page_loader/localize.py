# coding=utf-8

"""
This library provides main functionality of the app.

Parce and save downloaded document.
Obtain, download and save local resources from downloaded document.
"""

from re import match, search

import requests
from bs4 import BeautifulSoup
from page_loader import filesystem, hyphenate

_DEFAULT_PARSER = 'html_parser'

# REGEX Patterns
NON_LOCAL_PATH_PATTERN = r'http(s)?://.*\/*'
HOST_PATTERN = r'http(s)?://[\w\d\.\-]*'
PATH_PATTERN = r'http(s)?://[\w\d\.\-]*'

# Postfixs
_RESOURCE_FILES_DIR = '_files'

LOCAL_RESOURCES = (
    'img',
    'link',
    'script',
)
_HREF = 'href'
_SRC = '_src'
_DEFAULT_SCHEME = 'https://'
_LEAD_SLASH = '/'


def url_normalize(url, scheme=_DEFAULT_SCHEME):
    """
    Add HTTPS scheme to URL if does not it contains.

    Args:
        url : str
            String contains URL
        scheme : str
            Scheme which add to URL

    Returns:
        url : str
            URL with leading HTTPS scheme
    """
    if not url.startswith('http'):
        return ''.join([scheme, url])
    return url


def _is_local(resource):
    """
    Figure out is the resource local (don't contain host in url).

    Args:
        resource : (class 'bs4.element.Tag')
            Object contains reference to resources (image, link or script).

    Returns:
        bool :
            Return True if resource object has reference without host,
            else return False
    """
    if resource.get(_HREF):
        path = resource.get(_HREF)
    elif resource.get(_SRC):
        path = resource.get(_SRC)
    else:
        return False
    if search(NON_LOCAL_PATH_PATTERN, path):
        return False
    return True


def get_resource_path(resource):
    """
    Obtain reference path to the local resource file.

    Args:
        resource : (class 'bs4.element.Tag')
            Object contains reference to resources (image, link or script).

    Returns:
        path : str
            String contains full path to resource file
            (excluding protocol and host)
    """
    if resource.get(_HREF):
        path = resource.get(_HREF)
    elif resource.get(_SRC):
        path = resource.get(_SRC)
    path = path.rsplit('?')[0]
    if path.startswith(_LEAD_SLASH):
        return path
    return ''.join([_LEAD_SLASH, path])


def set_new_resource_link_on_doc(resource, new_link):
    """
    Update resource object reference to downloaded file.

    Args:
        resource : (class 'bs4.element.Tag')
            Object contains reference to resources (image, link or script).
        new_link : str
            New reference to downloaded resource file.

    Returns:
        resource : (class 'bs4.element.Tag)
            Updates resource object
    """
    if resource.attrs[_HREF]:
        resource.attrs[_HREF] = new_link
    elif resource.attrs(_SRC):
        resource.attrs[_SRC] = new_link

    return resource


def localize(document, output):  # noqa: WPS210
    """
    Parce and save local resources from document.

    Update downloaded document.

    Args:
        document : (class 'requests.models.Response)
            Downloaded document object
        output : str
            Destination directory for downloaded files

    Returns: None

    """
    # Get document DOM
    document_dom = BeautifulSoup(document.content, _DEFAULT_PARSER)

    # Obtain host of document
    document_host = match(
        HOST_PATTERN,
        url_normalize(document.url),
    ).group()

    # Obtain list of local resources
    resource_list = list(filter(
        _is_local,
        document_dom.find_all(LOCAL_RESOURCES),
    ),
    )

    # Create directory for resource files if local resources exist
    if resource_list:
        resource_dir = filesystem.create_dir(
            output=_LEAD_SLASH.join(
                output,
                hyphenate.make_resource_dir_name(document.url),
            ),
        )
    # Download each local resource from resource list
    for resource in resource_list:
        resource_path = get_resource_path(resource)
        downloaded_resource = requests.get(
            url_normalize(
                '{host}{path}'.format(
                    host=document_host,
                    path=resource_path,
                ),
            ),
        )

        if downloaded_resource:
            # Create new resource filename
            # with hyphen instead non-alphanumeric symbols
            resource_filename = hyphenate.make_resource_filename(
                resource_path,
            )
            # Save downloaded resource file
            filesystem.save_document(
                document_content=downloaded_resource.content,
                path=resource_dir,
                filename=resource_filename,
            )
            # Update resource reference in main document
            set_new_resource_link_on_doc(
                resource,
                resource_filename,
            )
    # Save modified document
    filesystem.save_document(
        document_content=document_dom,
        path_file=_LEAD_SLASH.join(
            output,
            hyphenate.make_document_name(document.url),
        ),
    )
