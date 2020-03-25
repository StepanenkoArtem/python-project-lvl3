import re

from bs4 import BeautifulSoup
from page_loader import download, save

SCHEME_PATTERN = r'http(s)?://'
TRAILING_SLASH = r'/*$'
REPLACABLE_SYMBOLS = r'[^-a-zA-Z0-9]'
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
    return None


def is_local(resource):
    return True


def get_resource_path(resource):
    if resource.attrs['href']:
        return resource.attrs['href']
    if resource.attrs['src']:
        return resource.attrs['src']
    return None


def make_resource_file_name(resource):
    return None


def localize_document(document, output):
    document_dom = BeautifulSoup(document.content, DEFAULT_PARSER)
    local_resources = list(filter(is_local, document_dom.find_all(RESOURCES)))
    resource_dir_name = hyphenate(document.url) + _FILES
    if local_resources:
        save.create_resource_dir(
            output=output,
            resource_dir_name=resource_dir_name,
        )
    for resource in local_resources:
        downloaded_resource = download.get_document(
            url='{domain}{path}'.format(
                domain=get_domain(document.url),
                path=get_resource_path(resource),
            ),
        )
        save.save_resource(
            resource_content=downloaded_resource.content,
            save_to='/'.join(
                output,
                resource_dir_name,
            ),
            filename=make_resource_file_name(get_resource_path),
        )
