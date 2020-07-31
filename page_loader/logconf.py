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
            _class: 'logging.handlers.RotatingFileHandler',
            _formatter: 'verbose',
            _level: 'INFO',
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
