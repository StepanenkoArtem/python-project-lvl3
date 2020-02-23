import os
import tempfile

from page_loader.download import get_requested
from page_loader.save import make_filename_from_url, save_requsted
from tests.get_data import get_data_from_json


def test_make_filename_from_url():
    filenames = get_data_from_json(
        'tests/data/save/uri_to_filename.json',
    )
    for url, expected in filenames.items():
        assert make_filename_from_url(url) == expected


def test_saving():  # noqa: WPS210
    list_names = []
    urls = get_data_from_json('tests/data/save/uri_to_filename.json')
    with tempfile.TemporaryDirectory() as temp_dir:
        for url, _ in urls.items():
            requested = get_requested(url)
            save_requsted(requested, temp_dir)
            list_names.append(make_filename_from_url(requested.url))
        temp_dir_files = os.listdir(temp_dir)
        for file_name in list_names:
            assert file_name in temp_dir_files
