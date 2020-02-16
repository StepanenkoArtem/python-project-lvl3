def validate_url(ctx, param, value):
    if 'https://' in value:
        return (value)
    else:
        raise click.BadParameter('Incorrect URL')


def validate_path(ctx, param, value):
    pass
