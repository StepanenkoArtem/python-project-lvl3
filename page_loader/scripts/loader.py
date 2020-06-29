#!/usr/bin/env python
# coding=utf-8

"""Main module. Retrive url from commandline args."""

from os import getcwd
from os.path import join

import click
import requests
from page_loader import localize

OK_STATUS = 200
DOWNLOAD_DIR = 'downloads'


@click.command()
@click.option(
    '--output',
    default=join(getcwd(), DOWNLOAD_DIR),
    help='Set destionation folder to save file',
)
@click.argument(
    'url',
)
def main(url, output):
    """Download web page from specified URL."""
    downloaded = requests.get(localize.url_normalize(url))
    if downloaded.status_code == OK_STATUS:
        localize.localize(downloaded, output)


if __name__ == '__main__':
    main()
