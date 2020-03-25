import os
import tempfile

import requests
from page_loader.save import save


def test_save():
    test_html = requests.get('https://hexlet.io')
    test_html.url = 'hexlet-io.html'
    temp_dir = tempfile.TemporaryDirectory()
    save(test_html, temp_dir.name)
    assert test_html.url in os.listdir(temp_dir.name)
