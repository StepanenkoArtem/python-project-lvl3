# coding=utf-8

"""
This library provides main functionality of the app.

Parce and save downloaded document.
Obtain, download and save local resources from downloaded document.
"""

from os.path import join
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from page_loader import filesystem, hyphenate

_DEFAULT_PARSER = 'html.parser'

# Postfixs
_RESOURCE_FILES_DIR = '_files'

LOCAL_RESOURCES = (
    'img',
    'link',
    'script',
)

RESOURCE_REFS = ('href', 'src')

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
    for attr in resource.attrs:
        if attr in RESOURCE_REFS:
            url_parts = urlparse(resource.get(attr))
            if url_parts.path == _LEAD_SLASH:
                return False
            if (not url_parts.netloc) and url_parts.path:
                return True
    return False


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
    for attr in RESOURCE_REFS:
        if resource.has_attr(attr):
            path = urlparse(resource.get(attr)).path
    if path.startswith(_LEAD_SLASH):
        return path
    return ''.join([_LEAD_SLASH, path])


def set_new_resource_link(resource, new_link):
    """
    Update resource object reference to downloaded file.

    Args:
        resource : (class 'bs4.element.Tag')
            Object contains reference to resources (image, link or script).
        new_link : str
            New reference to downloaded resource file.

    Returns:
        resource : (class 'bs4.element.Tag')
            Updates resource object
    """
    for attr in RESOURCE_REFS:
        if resource.has_attr(attr):
            resource.attrs[attr] = new_link
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

    # Obtain url components
    document_host = urlparse(document.url).netloc

    # Obtain list of local resources
    resource_list = list(filter(
        _is_local,
        document_dom.find_all(LOCAL_RESOURCES),
    ),
    )

    # Create directory for resource files if local resources exist
    if resource_list:
        resource_dir = filesystem.create_dir(
            dir_path=join(
                output,
                hyphenate.make_resource_dir_name(
                    document.url,
                ),
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
            resource_local_filename = hyphenate.make_resource_filename(
                resource_path,
            )
            localized_path = _LEAD_SLASH.join(
                [resource_dir, resource_local_filename],
            )
            # Save downloaded resource file
            filesystem.save_document(
                document_content=downloaded_resource.content,
                path_file=localized_path,
            )
            # Update resource reference in main document
            set_new_resource_link(
                resource,
                localized_path,
            )
    # Save modified document
    filesystem.save_document(
        document_content=document_dom.encode(),
        path_file=join(
            output,
            hyphenate.make_document_name(document.url),
        ),
    )
