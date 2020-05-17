import json

import mock
import pytest
from bs4 import BeautifulSoup
from page_loader import localize


def test_is_local():
    tests = {
        'https://httpbin.org/images': False,
        'https://httpbin.org/images/favicon.ico': False,
        '/images/favicon.ico': True,
        '/resources/scripts/jquery-2.3-4.min.js': True,
        'resources/scripts/jquery-2.3-4.min.js': True,
    }



@pytest.fixture()
def domains_data():
    with open('tests/data/localize/get_domain.json') as test_data_json:
        return json.load(test_data_json)


def test_get_domain(domains_data):
    for url, expected_domain in domains_data.items():
        assert expected_domain == localize.get_domain(url)


@pytest.fixture()
def hyphenate_data():
    with open('tests/data/localize/hyphenate.json') as test_data_json:
        return json.load(test_data_json)


def test_hyphenate(hyphenate_data):
    for url, expected_name in hyphenate_data.items():
        assert expected_name == localize.hyphenate(url)


def test_get_resource_path():
    expexted = [
        '/assets/favicon.ico',
        '/assets/application.css',
        '/packs/css/41-542.css',
        '/assets/tour_2.jpg',
        '/assets/tour_2.jpg',
        '/assets/landings.js',
        'https://another.domain.com/packs/js/runtime~landings.js',
        '/packs/js/2.js',
        '/packs/js/landings',
    ]
    with open('tests/data/localize/doc_before.html') as test_html_file:
        test_html = test_html_file.read()
    test_html_dom = BeautifulSoup(test_html, localize.DEFAULT_PARSER)
    for resource in test_html_dom.find_all(localize.RESOURCES):
        assert localize.get_resource_path(resource) in expexted


def test_make_resource_filename():
    tests = {
        '/assets/favicon.ico': 'assets-favicon.ico',
        '/assets/application.min2.css': 'assets-application-min2.css',
        'packs/css/41_542.css': 'packs-css-41_542.css',
        '/assets/tour_2.jpg': 'assets-tour_2.jpg',
        '/packs/js/2.min.js': 'packs-js-2-min.js',
    }
    for path, expected_filename in tests.items():
        assert expected_filename == localize.make_resource_filename(path)
