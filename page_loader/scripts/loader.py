#!/usr/bin/env python

from os import getcwd

import click
from page_loader import download, localize

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
    downloaded = download.get_document(url)
    if downloaded.status_code == OK_STATUS:
        localize.localize(downloaded, output)
    print(downloaded.url, downloaded.reason)


if __name__ == '__main__':
    main()
