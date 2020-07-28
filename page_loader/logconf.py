# coding=utf-8

"""Configure logging."""
_class = 'class'
_format = 'format'
_formatter = 'formatter'
_level = 'level'

log_conf = {
    'version': 1,
    'formatters': {
        'simple': {
            _class: 'logging.Formatter',
            _format: '%(levelname)s: %(message)s',
        },
        'verbose': {
            _class: 'logging.Formatter',
            _format: '%(asctime)s: %(name)s - %(levelname)s : %(message)s',
        },
    },
    'handlers': {
        'console': {
            _class: 'logging.StreamHandler',
            _formatter: 'simple',
            _level: 'DEBUG',
        },
        'logfile': {
            _class: 'logging.FileHandler',
            _formatter: 'verbose',
            _level: 'DEBUG',
            'filename': 'default.log',
        },
    },
    'loggers': {
        'page_loader': {
            _level: 'ERROR',
            'handlers': ['logfile', 'console'],
        },
    },
}
