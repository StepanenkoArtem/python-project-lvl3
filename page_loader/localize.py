import re

from bs4 import BeautifulSoup
from page_loader import download, save

SCHEME_PATTERN = r'http(s)?://'
TRAILING_SLASH = r'/*$'
START_SLASH = r'^/*'
REPLACABLE_SYMBOLS = r'[^_a-zA-Z0-9]'
DOMAIN = r'http(s)?://.[^\/\"]*'
IS_LOCAL = r'^/?[a-zA-Z0-9/\.-]*$'

_HTML = '.html'
_FILES = '_files'

HREF = 'href'
SRC = 'src'

DEFAULT_PARSER = 'html.parser'

RESOURCES = (
    'img',
    'link',
    'script',
)


def hyphenate(url):
    unschemed = re.sub(SCHEME_PATTERN, '', url)
    untrailed = re.sub(TRAILING_SLASH, '', unschemed)
    return re.sub(REPLACABLE_SYMBOLS, '-', untrailed)


def get_domain(url):
    found = re.search(DOMAIN, url)
    if found:
        return found.group(0)
    return None


def is_local(resource):
    for key in (SRC, HREF):
        if resource.has_attr(key):
            path = resource.attrs[key]
        return False
    if re.search(IS_LOCAL, path):
        return True
    return False


def get_resource_path(resource):
    for source in (SRC, HREF):
        if resource.has_attr(source):
            return resource.attrs[source]
    return None


def make_resource_filename(resource_path):
    basename, file_ext = resource_path.rsplit('.', 1)
    unslashed = re.sub(START_SLASH, '', basename)
    return '.'.join([re.sub(REPLACABLE_SYMBOLS, '-', unslashed), file_ext])


def update_resource_path(resource, local_path):
    for source in (SRC, HREF):
        if resource.has_attr(source):
            resource.attrs[source] = local_path
            return resource.attrs[source]
    return None


def localize_document(document, output):  # noqa: WPS210
    save.create_output_dir(output)
    document_dom = BeautifulSoup(document.content, DEFAULT_PARSER)
    local_resources = list(filter(is_local, document_dom.find_all(RESOURCES)))
    if local_resources:
        resource_dir = save.create_resource_dir(
            output=output,
            resource_dir_name=hyphenate(document.url) + _FILES,
        )
        for resource in local_resources:
            resource_path = get_resource_path(resource.attrs)
            downloaded_resource = download.get_document(
                url='{domain}{path}'.format(
                    domain=get_domain(document.url),
                    path=resource_path,
                ),
            )
            resource_local_filepath = save.save_document(
                document_content=downloaded_resource.content,
                path=resource_dir,
                filename=make_resource_filename(resource_path),
            )
            update_resource_path(resource, resource_local_filepath)
    save.save_document(
        document_content=document_dom.encode(),
        path=output,
        filename=hyphenate(document.url) + _HTML,
    )
