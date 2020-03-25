#!/usr/bin/env python

from os import getcwd

import click
from page_loader import download, localize


@click.command()
@click.option(
    '--save-to',
    default=getcwd(),
)
@click.argument(
    'url',
)
def main(url, save_to):
    document = download.get_document(url)
    localize.localize_document(document, save_to)


if __name__ == '__main__':
    main()
