# coding=utf-8

"""
This library provides main functionality of the app.

Parce and save downloaded document.
Obtain, download and save local resources from downloaded document.
"""

import logging
import os
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from page_loader import download, filesystem, hyphenate, settings
from progress.bar import FillingSquaresBar

LEAD_SLASH = '/'

logger = logging.getLogger(__name__)


def url_normalize(url, scheme=settings.DEFAULT_SCHEME):
    """
    Add HTTPS scheme to URL if does not it contains.

    Args:
        url : str
            String contains URL
        scheme : str
            Scheme which addEXIT_FS_ERRL

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
        if attr in settings.RESOURCE_REFS:
            url_parts = urlparse(resource.get(attr))
            scheme_n_netloc = url_parts.netloc or url_parts.scheme
            if len(url_parts.path) > 1 and not scheme_n_netloc:
                return True
    return False


def get_path_from_url(resource):
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
    logger.debug('')
    for attr in settings.RESOURCE_REFS:
        if resource.has_attr(attr):
            path = urlparse(resource.get(attr)).path
    if path.startswith(LEAD_SLASH):
        return path
    return ''.join([LEAD_SLASH, path])


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
    for attr in settings.RESOURCE_REFS:
        if resource.has_attr(attr):
            logger.debug('Set new resource link {link}'.format(link=new_link))
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
    document_dom = BeautifulSoup(document.content, settings.DEFAULT_PARSER)
    # Obtain list of local resources
    local_resources = list(
        filter(
            _is_local,
            document_dom.find_all(settings.LOCAL_RESOURCES),
        ),
    )

    # Create directory for resource files if local resources exist
    if local_resources:
        resource_dir = os.path.join(
            output,
            hyphenate.make_resource_dir_name(document.url),
        )
        filesystem.create_dir(resource_dir)

    # Get resource content and save it to local filesystem
    with FillingSquaresBar(
        settings.BAR_CAPTION,
        max=len(local_resources) if local_resources else 1,
    ) as counter:
        for resource in local_resources:
            resource_urlpath = get_path_from_url(resource)
            resource_filepath = os.path.join(
                output,
                hyphenate.make_resource_filename(resource_urlpath),
            )

            try:
                filesystem.save_document(
                    document_content=download.download(
                        url=urljoin(document.url, resource_urlpath),
                    ).content,
                    filepath=resource_filepath,
                )
            except ConnectionError:
                logger.warning(
                    'Cannot download resource {res}'.format(
                        res=resource_urlpath,
                    ),
                )

            set_new_resource_link(
                resource=resource,
                new_link=resource_filepath,
            )
            counter.next()  # noqa: B305
        counter.finish()
    # Save modified document
    filesystem.save_document(
        document_content=document_dom.encode(),
        filepath=os.path.join(
            output,
            hyphenate.make_document_name(document.url),
        ),
    )
