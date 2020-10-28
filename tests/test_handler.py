# coding=utf-8

"""Testing handler.py module."""

import os

from bs4 import BeautifulSoup
from loader import handler, path


def test_update_resource():
    """Check is resource location update correctly."""
    # PREPARE
    expected_dom = BeautifulSoup(
        open(
            'tests/pages/expected/stepanenkoartem-github-io.html',
            'rb',
        ).read(),
        'html.parser',
    )

    actual_dom = BeautifulSoup(
        open(
            'tests/pages/origin/stepanenkoartem.github.io.html',
            'rb',
        ).read(),
        'html.parser',
    )
    # EXCERSIZE
    for resource in handler.get_resources(actual_dom):
        handler.update_resource(
            resource,
            new_link=os.path.join(
                'stepanenkoartem-github-io_files',
                path.for_resource(handler.get_path(resource)),
            ),
        )
    # CHECK
    assert expected_dom == actual_dom
