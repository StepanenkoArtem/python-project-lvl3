#!/usr/bin/env python

from os import getcwd

import click
from page_loader import download, save
# from page_loader.get_resources import get_resources
from page_loader.localize import localize


@click.command()
@click.option(
    '--save-to',
    default=getcwd(),
)
@click.argument(
    'url',
)
def main(url, save_to):
    downloaded = download.get_document(url)
    localized = localize(downloaded)
    save.save_html(localized, save_to)
    # resource_files = download.get_resources(downloaded)
    # save.save_resources(resource_files, save_to)


if __name__ == '__main__':
    main()
