# coding=utf-8

"""Logging configuration."""


VERBOSE_FORMAT = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
SIMPLE_FORMAT = '%(levelname)s:%(message)s'
DEFAULT_LOGGER = __package__


dict_config = {
    'version': 1,
    'formatters': {
        'simple': {
            'class': 'logging.Formatter',
            'format': SIMPLE_FORMAT,
        },
        'verbose': {
            'class': 'logging.Formatter',
            'format': VERBOSE_FORMAT,
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': 'WARNING',
        },
        'file_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'level': 'DEBUG',
            'filename': 'logging.log',
        },
    },
    'loggers': {
        DEFAULT_LOGGER: {
            'level': 'DEBUG',
            'handlers': ['file_handler', 'console'],
        },
    },
}
