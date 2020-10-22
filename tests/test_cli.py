# coding=utf-8

"""Test main functionality."""

import os
import tempfile

import pytest
from loader import cli

TEMP_DOWNLOADS = tempfile.mkdtemp()
TEST_DIR = 'tests/golden'
URL = 'https://stepanenkoartem.github.io/'


@pytest.fixture(scope='module')
def testpage():
    """Download test data from URL for further tests."""
    cli.main(
        url=URL,
        output=TEMP_DOWNLOADS,
    )


def test_names():
    """Compare downloaded page content to golden files."""
    expected = []
    actual = []
    for _, _, expected_files in list(os.walk(TEST_DIR)):
        expected.extend(expected_files)

    for _, _, actual_files in list(os.walk(TEMP_DOWNLOADS)):
        actual.extend(actual_files)

    assert expected == actual
    assert os.listdir(TEST_DIR) == os.listdir(TEMP_DOWNLOADS)


def test_content():
    """Compare HTML content in golden and downloaded documents."""
    expected = open(
        'tests/golden/stepanenkoartem-github-io.html', mode='rb',
    )
    actual = open(
        os.path.join(TEMP_DOWNLOADS, 'stepanenkoartem-github-io.html'),
        mode='rb',
    )
    assert expected.read() == actual.read()
