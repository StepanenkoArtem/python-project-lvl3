import json

from page_loader.localize import make_name_from


def test_make_name_from():
    test_data_file = 'tests/data/localize/url_to_name.json'
    with open(test_data_file) as test_data_json:
        test_data = json.load(test_data_json)
    for url, expected_name in test_data.items():
        received_name = make_name_from(url)
        assert expected_name == received_name
