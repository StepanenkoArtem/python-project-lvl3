#!/usr/bin/env python

import click
from page_loader.download import get_requested
from page_loader.save import save_content
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
    default='./page-downloads',
    help='Enter path to folder to save downloading pages',
    callback=validate,
)
@click.argument(
    'url',
    callback=validate,
)
def main(save_to, url):
    requested_data = get_requested(url)
    save_content(requested_data, save_to)


if __name__ == '__main__':
    main()
