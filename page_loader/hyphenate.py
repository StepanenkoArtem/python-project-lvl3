import re

# Postfixes
_DOC_EXTENSION = '.html'
_RES_DIR_POSTFIX = '_files'

# REGEX Patterns
_HYPHENATE_PATTERN = r'[^0-9a-zA-Z]'
_FILE_EXTENSION = r'(?=\.)[^/]*?$'

_HYPHEN = '-'
_LEADING_SLASH = '/'


def _hyphenate(sequence):
    return re.sub(_HYPHENATE_PATTERN, _HYPHEN, sequence)


def _trim_extension(url):
    return re.sub(_FILE_EXTENSION, '', url.strip(_LEADING_SLASH))


def make_resource_dir_name(document_url):
    return '{file_basename}{ext}'.format(
        file_basename=_hyphenate(_trim_extension(document_url)),
        ext=_RES_DIR_POSTFIX,
    )


def make_resource_filename(resource_path):
    extension = re.search(_FILE_EXTENSION, resource_path).group(0)
    return '{base_path}{ext}'.format(
        base_path=_hyphenate(_trim_extension(resource_path)),
        ext=extension,
    )


def make_document_name(document_url):
    return '{file_basename}{ext}'.format(
        file_basename=_hyphenate(_trim_extension(document_url)),
        ext=_DOC_EXTENSION,
    )
