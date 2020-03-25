from page_loader import localize
from tests.get_test_data import _get_test_data_from_json


def test_get_domain():
    test_data_file = 'tests/data/localize/get_domain.json'
    test_data = _get_test_data_from_json(test_data_file)
    for url, expected_domain in test_data.items():
        received_domain = localize.get_domain(url)
        assert expected_domain == received_domain


def test_hyphenate():
    test_data_file = 'tests/data/localize/make_name_from.json'
    test_data = _get_test_data_from_json(test_data_file)
    for url, expected_name in test_data.items():
        received_name = localize.hyphenate(url)
        assert expected_name == received_name


def test_is_local():
    assert expected == recieved


def test_get_resource_path(resource):
    assert expected == recieved


def test_make_resource_filename():
    assert expected == recieved


def test_localize_resource():
    assert expected == recieved
