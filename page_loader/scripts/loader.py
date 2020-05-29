#!/usr/bin/env python

from os import getcwd

import click
from page_loader import download, localize


@click.command()
@click.option(
    '--output',
    default=getcwd(),
)
@click.argument(
    'url',
)
def main(url, output):
    downloaded = download.get_document(url)
    if downloaded:
        localize.localize(downloaded, output)


if __name__ == '__main__':
    main()
