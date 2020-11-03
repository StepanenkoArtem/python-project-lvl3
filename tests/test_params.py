# coding=utf-8

"""This module provide test for check is user input correct arguments."""

import pytest
from loader import cli

PATH_TEST_CASES = (
    '/my.log',
    '/usr/my.log',
)
LEVEL_VALID_CASES = (
    '10',
    10,
    'Warning',
    'WARNING',
    'critical',
    'deBug',
)


@pytest.mark.parametrize(
    'path',
    PATH_TEST_CASES,
)
def test_check_path(path):
    """Test logfile checking.

    Args:
        path: str
            testing value of logfile path
    """
    with pytest.raises(cli.ParamError):
        cli.check_path('', '', path)
