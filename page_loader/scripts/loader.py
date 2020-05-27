#!/usr/bin/env python

from os import getcwd

import click
from page_loader import download, localize, save


@click.command()
@click.option(
    '--save-to',
    default=getcwd(),
)
@click.argument(
    'url',
)
def main(url, save_to):
    downloaded_document = download.get_document(url)
    localized_document = localize.localize_document(downloaded_document)
    save.save_document(localized_document)


if __name__ == '__main__':
    main()
