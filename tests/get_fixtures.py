import json


def get_fixture_from_json(path_to_fixtures_file):
    with open(path_to_fixtures_file) as fixture:
        return json.load(fixture)
