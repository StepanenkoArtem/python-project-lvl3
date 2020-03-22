import os

# File operations modes
WB = 'wb'


def save_html(document, save_to):
    if not os.path.isabs(save_to):
        save_to = os.path.join(os.getcwd(), save_to)
        save_to = os.path.abspath(os.path.normpath(save_to))
    if not os.path.exists(save_to):
        os.makedirs(save_to)
    html_file_path = os.path.join(save_to, document.url)
    with open(html_file_path, mode=WB) as html_file:
        html_file.write(document.content)


def save_resources(*resource_files, save_to):
    return None
