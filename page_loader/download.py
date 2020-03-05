from re import sub

import requests

CLEAN_URL_REGEX = r'[-\?\#\@].*$'


def _clean_url(url):
    return sub(CLEAN_URL_REGEX, '', url)


def download(url):
    try:
        return requests.get(_clean_url(url))
    except requests.exceptions.RequestException:
        return None
