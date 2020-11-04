# coding=utf-8

"""This module provide test for check is user input correct arguments."""

import pytest
from loader import cli

PATH_TEST_CASES = (
    '/my.log',
    '/usr/my.log',
)
LEVEL_VALID_CASES = (
    ('10', 10),
    ('20', 20),
    ('Warning', 'WARNING'),
    ('WARNING', 'WARNING'),
    ('critical', 'CRITICAL'),
    ('deBug', 'DEBUG'),
    ('info', 'INFO'),
    ('Not_set', 'NOT_SET'),
    ('error', 'ERROR'),
    ('Error', 'ERROR'),
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


@pytest.mark.parametrize(
    'level_string, level_int',
    LEVEL_VALID_CASES,
)
def test_check_level(level_string, level_int):
    """Validate logging level.

    Args:
        level_string : str
            user-input level
        level_int : int
            valid logging level in integer
    """
    assert cli.check_level('', 'level', level_string) == level_int
