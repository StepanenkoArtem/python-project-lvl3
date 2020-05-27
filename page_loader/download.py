import requests

DEFAULT_SCHEME = 'https://'


def _url_normalize(url, scheme=DEFAULT_SCHEME):
    if not url.startswith('http'):
        return ''.join([scheme, url.split('?')[0]])
    return url.split('?')[0]


def get_document(url):
    return requests.get(_url_normalize(url))
