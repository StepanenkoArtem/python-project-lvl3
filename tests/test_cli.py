# coding=utf-8

"""Test main functionality."""

import os
import tempfile

import pytest
from bs4 import BeautifulSoup
from loader import cli, path

TEMP_DIR = tempfile.mkdtemp()
EXPECTED = 'tests/pages/expected'
URL = 'https://stepanenkoartem.github.io/'


@pytest.fixture(scope='session', autouse=True)
def testrun():
    """Run main function.

    Returns:
        :None
    """
    try:
        cli.main(
            [URL, '--output', TEMP_DIR],
        )
    except SystemExit:
        return None


def test_content():
    """Compare expected and downloaded html content."""
    # PREPARE
    expected_f = open(
        'tests/pages/expected/stepanenkoartem-github-io.html',
        'rb',
    )
    expected_dom = BeautifulSoup(
        expected_f.read(),
        'html.parser',
    )

    actual_f = open(
        os.path.join(TEMP_DIR, path.for_page(URL)),
    )
    actual_dom = BeautifulSoup(actual_f, 'html.parser')

    # CHECK
    assert actual_dom.decode() == expected_dom.decode()


def test_resource_files():
    """Check is resource files was download correctly."""
    expected_files = os.listdir(EXPECTED)
    actual_files = os.listdir(TEMP_DIR)
    assert expected_files == actual_files
