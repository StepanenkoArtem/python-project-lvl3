#!/usr/bin/env python

from os import getcwd

import click
from page_loader.download import download
from page_loader.localize import localize
from page_loader.save import save


@click.command()
@click.option(
    '--save-to',
    default=getcwd(),
)
@click.argument(
    'url',
)
def main(url, save_to):
    downloaded = download(url)
    localized = localize(downloaded)
    save(localized, save_to)


if __name__ == '__main__':
    main()
