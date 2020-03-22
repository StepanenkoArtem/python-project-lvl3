import json

from page_loader.download import get_document, url_normalize


def test_url_cleanup():
    test_data_file = 'tests/data/download/url_normalize.json'
    with open(test_data_file) as test_data_json:
        test_data = json.load(test_data_json)
    for url, expected_url in test_data.items():
        received_url = url_normalize(url)
        assert expected_url == received_url


def test_get_document():
    test_data_file = 'tests/data/download/get_document.json'
    with open(test_data_file) as test_data_json:
        test_data = json.load(test_data_json)
    for url, expected_code in test_data.items():
        received_code = get_document(url).status_code
        assert expected_code == received_code
