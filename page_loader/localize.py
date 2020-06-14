from re import match, search

import requests
from bs4 import BeautifulSoup
from page_loader import filesystem, hyphenate

NON_LOCAL_PATH_PATTERN = r'http(s)?://.*\/*'
HOST_PATTERN = r'http(s)?://[\w\d\.\-]*'
PATH_PATTERN = r'http(s)?://[\w\d\.\-]*'
LOCAL_RESOURCES = (
    'img',
    'link',
    'script',
)
_RESOURCE_FILES_DIR = '_files'
_DEFAULT_PARSER = 'html_parser'
_HREF = 'href'
_SRC = '_src'
_DEFAULT_SCHEME = 'https://'
_START_SLASH = '/'


def url_normalize(url, scheme=_DEFAULT_SCHEME):
    if not url.startswith('http'):
        return ''.join([scheme, url])
    return url


def _is_local(resource):
    if resource.get(_HREF):
        path = resource.get(_HREF)
    elif resource.get(_SRC):
        path = resource.get(_SRC)
    else:
        return False
    if search(NON_LOCAL_PATH_PATTERN, path):
        return False
    return True


def get_document_host(document_url):
    """
    Obtain downloaded document host including protocol.

    Args:
        document_url (str): Contain url of downloaded document.

    Returns:
        (str): String contains host ('http(s)://') of downloaded document.
    """
    matched_host = match(HOST_PATTERN, url_normalize(document_url))
    return matched_host.group()


def get_resource_path(resource):
    if resource.get(_HREF):
        path = resource.get(_HREF)
    elif resource.get(_SRC):
        path = resource.get(_SRC)
    path = path.rsplit('?')[0]
    if path.startswith(_START_SLASH):
        return path
    return ''.join([_START_SLASH, path])


def set_new_resource_link_on_doc(resource, filename):
    return filename


def localize(document, output):  # noqa: WPS210
    document_dom = BeautifulSoup(document.content, _DEFAULT_PARSER)
    document_host = get_document_host(document.url)
    resource_list = list(filter(
        _is_local,
        document_dom.find_all(LOCAL_RESOURCES),
    ),
    )
    if resource_list:
        resource_dir = filesystem.create_dir(
            output=_START_SLASH.join(
                output,
                hyphenate.make_resource_dir_name(document.url),
            ),
        )
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
            resource_filename = hyphenate.make_resource_filename(
                resource_path,
            )
            filesystem.save_document(
                document_content=downloaded_resource.content,
                path=resource_dir,
                filename=resource_filename,
            )
            set_new_resource_link_on_doc(resource, resource_filename)
    filesystem.save_document(
        document_content=document_dom,
        path_file=_START_SLASH.join(
            output,
            hyphenate.make_document_name(document.url),
        ),
    )
