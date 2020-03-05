import os
from re import sub

from page_loader import settings

_CUT_SCHEME = r'http(s)?:\/\/'
_CUT_TRAILING_SLASH = r'/$'
_SUB_TO_HYPHEN = r'[\./_]'


def get_full_path(output):
    return os.path.normpath(os.path.abspath(output))


def convert_url(url):
    url = sub(_CUT_SCHEME, '', url)
    url = sub(_CUT_TRAILING_SLASH, '', url)
    return sub(_SUB_TO_HYPHEN, '-', url)


def get_html_file_name():
    return None


def get_html_file_path(url, save_to):
    return None


def get_resource_file_path():
    return None


def get_resource_dir_name():
    return None


def create_resource_dir(url, destination_dir):
    return None
