#!/usr/bin/env python

import click
from page_loader import settings
from page_loader.download import get_requested
from page_loader.save import CURRENT_DIR, save_requsted
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
    default=CURRENT_DIR,
    help=settings.PATH_HELP,
    callback=validate,
)
@click.argument(
    'url',
    callback=validate,
)
def main(url, save_to):
    requested = get_requested(url)
    if requested:
        save_requsted(requested, save_to)
    else:
        print(settings.CON_ERR)  # noqa: T001


if __name__ == '__main__':
    main()
