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
)
@click.argument(
    'url',
)
def main(url, output):
    """
    Get url from command-line arguments.

    Args:
        url : str
            String contains url.
        output : str
            String contains destination path to save downloaded doc.

    Returns: None
    """
    downloaded = requests.get(localize.url_normalize(url))
    if downloaded.status_code == OK_STATUS:
        localize.localize(downloaded, output)


if __name__ == '__main__':
    main()
