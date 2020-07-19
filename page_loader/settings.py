# coding=utf-8

"""Settings."""
STATUS_OK = 200
DEFAULT_DOWNLOAD_DIR = 'downloads'
LOCAL_RESOURCES = (
    'img',
    'link',
    'script',
)
DEFAULT_PARSER = 'html.parser'

RESOURCE_FILES_DIR = '_files'

RESOURCE_REFS = ('href', 'src')

DEFAULT_SCHEME = 'https://'

# Logging
LOG_CONF = 'page_loader/logging.yaml'
DEFAULT_FORMATTER = '%(asctime)s: %(name)s - %(levelname)s : %(message)s'
DEFAULT_LOGGER = 'page_loader'

# Logging messages

# __main__
DEB_USER_LOGGER = 'Create user logging handler'

# download
DEB_DL_URL_GET = 'Retrieve URL={url}'
ERR_DL_CONNECTTION = 'Cannot establish connection with {url}'
# filesystem

# hyphenate
DEB_HYPH_HYPHENATE = 'Replace non-aplhanumeric symbols to hyphen in {path}'
DEB_HYPH_TRIM_EXT = 'Trim file extension on {path}'
DEB_HYPH_MAKE_DIR = 'Make resource directory name from url {url}'
DEB_HYPH_MAKE_RES_FILENAME = 'Make new resource filename from path {path}'
DEB_HYPH_EXT_NOT_EXIST = 'File extension does not exist'
DEB_HYPH_FILENAME = 'Make new document name'

# localize
DEB_LOC_GET_DOM = 'Get DOM from downloaded document'
DEB_LOC_GET_RES_LIST = 'Obtain resource list'
DEB_LOC_GET_HOST = 'Get downloaded document host'
DEB_DOWNLOAD_RES = 'Start downloading resourses'
WARN_RES_ISNT_FOUND = 'Cannot retrive resource {res}'
