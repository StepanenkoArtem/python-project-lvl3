# coding=utf-8

import os

import pytest
from bs4 import BeautifulSoup
from page_loader import download
from page_loader.localize import localize

RESOURCES = ('link', 'script', 'img')
PARSER = 'html.parser'


@pytest.fixture()
def golden():
    """
    Get reference HTML from golden file.

    Returns:
        bytes: html content
    """
    with open('tests/golden/stepanenkoartem-github-io.html', 'rb') as html:
        return html.read(), os.listdir('tests/golden')


@pytest.fixture()
def downloaded(tmpdir):
    """
    Get downloaded html files and resource files.

    Args:
        tmpdir: builtin pytest fixture

    Returns:
        bytes: downloaded and modified html content
        list: list of downloaded resource files
    """
    output = tmpdir
    url = 'https://stepanenkoartem.github.io'
    localize(download.get_page(url), output)
    with open(
        output.join('/stepanenkoartem-github-io.html'),
        'rb',
    ) as downloaded:
        return downloaded.read(), os.listdir(output)


def test_modified_document(golden, downloaded):
    """
    Checking is downloaded document was modified correctly.

    Args:
        golden: fixture returns golden html files and resource files
        downloaded: fixture returns downloaded html and resource files
    """
    golden_html, _ = golden
    downloaded_html, _ = downloaded

    golden_resources = BeautifulSoup(
        golden_html, PARSER,
    ).findAll(RESOURCES)

    downloaded_resources = BeautifulSoup(
        downloaded_html, PARSER,
    ).findAll(RESOURCES)

    assert golden_resources == downloaded_resources


def test_downloaded_resources(golden, downloaded):
    """
    Check equality downloaded and golden resource files.

    Args:
        golden: fixture returns golden html files and resource files
        downloaded: fixture returns downloaded html and resource files
    """
    _, golden_files = golden
    _, downloaded_files = downloaded
    assert golden_files == downloaded_files
