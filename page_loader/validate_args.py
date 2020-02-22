import re

URL_REGEX = r'^http(s)?:\/\/[\w/]*\.[\w\.\/\&\?=]*$'
PATH_REGEX = r'(^.([-\w/~])*$)'


def _validate_url(url):
    if re.search(URL_REGEX, url):
        return True
    return False


def _validate_path(save_to):
    # need to refactor (to REGEX) later
    if re.search(PATH_REGEX, save_to) and '//' not in save_to:
        return True
    return False


def is_valid(option, option_value):
    if option.name == 'url':
        return _validate_url(option_value)
    if option.name == 'save_to':
        return _validate_path(option_value)
    return False
