import re

from bs4 import BeautifulSoup
from page_loader import download, save

SCHEME_PATTERN = r'http(s)?://'
TRAILING_SLASH = r'/*$'
REPLACABLE_SYMBOLS = r'[^-a-zA-Z0-9]'
DOMAIN = r'http(s)?://.[^\/\"]*'

_HTML = '.html'
_FILES = '_files'

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
    return True


def get_resource_path(resource):
    if resource.attrs['href']:
        return resource.attrs['href']
    if resource.attrs['src']:
        return resource.attrs['src']
    return None


def make_resource_filename(resource):
    return None


def localize_resource(resource, filename):
    return None


def localize_document(document, output):  # noqa: WPS210
    document_dom = BeautifulSoup(document.content, DEFAULT_PARSER)
    local_resources = list(filter(is_local, document_dom.find_all(RESOURCES)))
    if local_resources:
        resource_dir = save.create_resource_dir(
            output=output,
            resource_dir_name=hyphenate(document.url) + _FILES,
        )
        for resource in local_resources:
            resource_path = get_resource_path(resource)
            downloaded_resource = download.get_document(
                url='{domain}{path}'.format(
                    domain=get_domain(document.url),
                    path=resource_path,
                ),
            )
            resource_file_path = save.save_resource(
                resource_content=downloaded_resource.content,
                save_to=resource_dir,
                filename=make_resource_filename(resource_path),
            )
            localize_resource(resource, resource_file_path)
    save.save_document(
        document=document_dom.encode(),
        path=output,
    )
