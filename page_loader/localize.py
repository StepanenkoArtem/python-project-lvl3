import re

SCHEME_PATTERN = r'http(s)?://'
REPLACABLE_SYMBOLS = r'[^-a-zA-Z0-9]'
FILE_EXT = '.html'


def make_name_from(url):
    unschemed = re.sub(SCHEME_PATTERN, '', url)
    hyphened = re.sub(REPLACABLE_SYMBOLS, '-', unschemed)
    return hyphened + FILE_EXT


def localize(document):
    document.url = make_name_from(document.url)
    return document
