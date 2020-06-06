import json


def get_dataset_from_file(data_set_file):
    with open(data_set_file) as test_data:
        return json.load(test_data).items()
