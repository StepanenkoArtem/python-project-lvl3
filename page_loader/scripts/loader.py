#!/usr/bin/env python

from os import getcwd

import click
from page_loader import settings
from page_loader.download import download
from page_loader.save import save
from page_loader.validate_args import is_valid


def validate(ctx, option, option_value):
    if is_valid(option, option_value):
        return option_value
    raise click.BadParameter(
        'Parameter {option} is not valid'.format(option=option.name),
    )


@click.command()
@click.option(
    '--save-to',
    default=getcwd(),
    help=settings.HELP_SAVE_TO,
    callback=validate,
)
@click.argument(
    'url',
    callback=validate,
)
def main(url, save_to):
    save(download(url), save_to)


if __name__ == '__main__':
    main()
