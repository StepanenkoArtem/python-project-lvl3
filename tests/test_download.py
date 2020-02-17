import json

from page_loader.download import get_web_content


def test_download():
    fixtures = 'tests/fixtures/download/urls.json'
    with open(fixtures) as expected_data:
        expected = json.load(expected_data)
        for url, status_code in expected.items():
            assert get_web_content(url).status_code == status_code
