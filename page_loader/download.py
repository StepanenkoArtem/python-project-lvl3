from re import sub

import requests

CLEAN_URL_REGEX = r'[-\?\#\@].*$'


def clean_url(url):
    return sub(CLEAN_URL_REGEX, '', url)


def get_requested(url):
    try:
        return requests.get(clean_url(url))
    except requests.exceptions.RequestException:
        return None
