import re

from bs4 import BeautifulSoup
from page_loader import download, filesystem, hyphenate

LOCAL_PATH_PATTERN = r'http(s)?://.*\/*'
LOCAL_RESOURCES = (
    'img',
    'link',
    'script',
)
_RESOURCE_FILES_DIR = '_files'

_HREF = 'href'
_SRC = '_src'


def _is_local(resource):
    if resource.get(_HREF):
        path = resource.get(_HREF)
    elif resource.get(_SRC):
        path = resource.get(_SRC)
    else:
        return False
    if re.search(LOCAL_PATH_PATTERN, path):
        return False
    return True


def _get_resource_url(resource):
    return None


def _get_resource_path(resource):
    return None


def _set_local_resource_filename(resource, new_entry):
    return None


def localize(document, output):  # noqa: WPS210
    document_dom = BeautifulSoup(document.content, 'html_parser')
    resource_list = list(filter(
        _is_local,
        document_dom.find_all(LOCAL_RESOURCES),
    ),
    )
    if resource_list:
        resource_dir = filesystem.create_resource_dir(
            output=output,
            resource_dir_name=hyphenate.make_resource_dir_name(
                document.url,
            ),
        )
    for resource in resource_list:
        downloaded_resource = download.get_document(
            _get_resource_url(resource),
        )
        resource_filename = hyphenate.make_resource_file_name(
            downloaded_resource.url,
        )
        if downloaded_resource:
            filesystem.save_document(
                document_content=downloaded_resource.content,
                path=resource_dir,
                filename=resource_filename,
            )
            _set_local_resource_filename(resource, resource_filename)
    filesystem.save_document(
        document_content=document_dom,
        path=output,
        filename=hyphenate.make_document_name(document.url),
    )
