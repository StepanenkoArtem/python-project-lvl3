import json


def _get_test_data_from_json(test_data_file):
    with open(test_data_file) as test_data_json:
        return json.load(test_data_json)
