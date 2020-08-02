# coding=utf-8

from page_loader.scripts.loader import _validate_level


def test_validate_level():  # noqa: D103, WPS437
    test_data = {
        'incorrect_level': 0,
        'debug': 10,
        'info': 20,
        'warning': 30,
        'error': 40,
        'critical': 50,
        'DEBUG': 10,
        'INFO': 20,
        'WARNING': 30,
        'ERROR': 40,
        'CRITICAL': 50,
        10: 10,
        20: 20,
        30: 30,
        40: 40,
        50: 50,
    }
    for level, expected in test_data.items():
        actual = _validate_level(None, None, level)
        assert expected == actual
