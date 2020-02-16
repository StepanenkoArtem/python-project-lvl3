#!/usr/bin/env python

import click
from page_loader.download import get_web_content
from page_loader.save import save_content
from page_loader.validate_args import validate_url, validate_path


@click.command()
@click.option(
    '--output',
    default='~/page-downloads',
    help='Enter path to folder to save downloading pages',
)
@click.argument('url', callback=validate_url)
def main(output, url):
    page = get_web_content(url)
    save_content(page)


if __name__ == '__main__':
    main()
