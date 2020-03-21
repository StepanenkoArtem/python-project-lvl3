import json

from page_loader.download import download

TEST_DATA_FILE = 'tests/data/_download.json'


def test_download():
    with open(TEST_DATA_FILE) as test_data_json:
        test_data = json.load(test_data_json)
    for url, expected_code in test_data.items():
        received_code = download(url).status_code
        assert expected_code == received_code
