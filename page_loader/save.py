import os
from re import sub

CURRENT_DIR = os.getcwd()
FILE_EXTENSION = '.html'
_CUT_SCHEME = r'http(s)?:\/\/'
_CUT_TRAILING_SLASH = r'/$'
_SUB_TO_HYPHEN = r'[\./_]'


def make_filename_from_url(url):
    url = sub(_CUT_SCHEME, '', url)
    url = sub(_CUT_TRAILING_SLASH, '', url)
    return sub(_SUB_TO_HYPHEN, '-', url) + FILE_EXTENSION


def _get_dir(path):
    path = os.path.expanduser(path)
    path = os.path.abspath(os.path.normpath(path))
    return path


def save_requsted(requested, save_to):
    filename = make_filename_from_url(requested.url)
    dir_path = _get_dir(save_to)
    full_path = os.path.join(dir_path, filename)
    with open(full_path, 'wb') as requested_page:
        requested_page.write(requested.content)
