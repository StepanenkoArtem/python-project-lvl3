#!/usr/bin/env python

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
    downloaded = requests.get(localize.url_normalize(url))
    if downloaded.status_code == OK_STATUS:
        localize.localize(downloaded, output)


if __name__ == '__main__':
    main()
