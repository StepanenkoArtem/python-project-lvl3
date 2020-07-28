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
DEFAULT_TIMEOUT = 3

RESOURCE_FILES_DIR = '_files'

RESOURCE_REFS = ('href', 'src')

DEFAULT_SCHEME = 'https://'

# ProgressBar settings
BAR_CAPTION = 'Loading resources'

# System exit codes

EXIT_CON_ERR = 1
EXIT_FS_ERR = 2
