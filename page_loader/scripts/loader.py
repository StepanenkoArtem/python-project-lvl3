#!/usr/bin/env python

import click
from page_loader.download import get_requested
from page_loader.save import save_requsted as save
from page_loader.validate_args import is_valid


def validate(ctx, option, option_value):
    if is_valid(option, option_value):
        return option_value
    raise click.BadParameter(
        'Parameter {option} is not valid'.format(option=option.name),
    )


@click.command()
@click.option(
    '--path',
    default='./page-downloads',
    help='Enter path to folder to save downloading pages',
    callback=validate,
)
@click.argument(
    'url',
    callback=validate,
)
def main(url, path):
    requested = get_requested(url)
    if requested:
        save(requested, path)
    else:
        print('Connection Failed')  # noqa: T001


if __name__ == '__main__':
    main()
