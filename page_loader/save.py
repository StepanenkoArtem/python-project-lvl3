import os
from re import sub

FILE_EXTENSION = '.html'
_CUT_SCHEME = r'http(s)?:\/\/'
_CUT_TRAILING_SLASH = r'/$'
_SUB_TO_HYPHEN = r'[\./_]'


def _make_filename_from_url(url):
    url = sub(_CUT_SCHEME, '', url)
    url = sub(_CUT_TRAILING_SLASH, '', url)
    return sub(_SUB_TO_HYPHEN, '-', url) + FILE_EXTENSION


def save_requsted(requested, path):
    print(requested.url)
    print(len(requested.text))
