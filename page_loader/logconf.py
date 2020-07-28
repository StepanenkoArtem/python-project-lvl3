# coding=utf-8

"""Logging configuration."""


_class = 'class'
_format = 'format'
_formatter = 'formatter'
_level = 'level'

DEFAULT_LOGFILE = 'logging.log'
VERBOSE_FORMAT = '%(asctime)s: %(name)s - %(levelname)s : %(message)s'
SIMPLE_FORMAT = '%(levelname)s: %(message)s'
DEFAULT_LOGGER = 'page_loader'

config_dict = {
    'version': 1,
    'formatters': {
        'simple': {
            _class: 'logging.Formatter',
            _format: SIMPLE_FORMAT,
        },
        'verbose': {
            _class: 'logging.Formatter',
            _format: VERBOSE_FORMAT,
        },
    },
    'handlers': {
        'console': {
            _class: 'logging.StreamHandler',
            _formatter: 'simple',
            _level: 'WARNING',
        },
        'logfile': {
            _class: 'logging.FileHandler',
            _formatter: 'verbose',
            _level: 'DEBUG',
            'filename': DEFAULT_LOGFILE,
        },
    },
    'loggers': {
        DEFAULT_LOGGER: {
            _level: 'WARNING',
            'handlers': ['logfile', 'console'],
        },
    },
}

# Logging messages

# __main__
DEB_USER_LOGGER = 'Create user logging handler'
CANNOT_READ_CONF = 'Cannot find logging.yaml file'

# download
DEB_DL_URL_GET = 'Retrieve URL={url}'
ERR_DL_CONNECTTION = 'Cannot establish connection with {url}'

# filesystem
DEB_FS_CREATE_DIR = 'Create resources subdirectory'
ERR_FS_PERMISSION_DND = 'Permission denied'
ERR_FS_CREATE_FILE_ERR = 'Cannot create file'

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
DEB_LOC_DOWNLOAD_RES = 'Start downloading resourses'
DEB_LOC_URL_NORM = 'Normalize url'
DEB_LOC_GET_RES_PATH = 'Get resource path'
DEB_LOC_SET_NEW_LINK = 'Update link'
WARN_LOC_RES_ISNT_FOUND = 'Cannot retrive resource {res}'
WARN_LOC_RES_TIMEOUT = 'Timeout error with downloading {res}'
