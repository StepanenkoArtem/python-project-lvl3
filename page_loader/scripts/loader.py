#!/usr/bin/env python
# coding=utf-8

"""Main module. Retrive url from commandline args."""

from os import getcwd

import click
import requests
from page_loader import localize

OK_STATUS = 200


@click.command()
@click.option(
    '--output',
    default=getcwd(),
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
