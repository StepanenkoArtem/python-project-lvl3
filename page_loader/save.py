import os

# File operations modes
WB = 'wb'


def create_resource_dir(output, resource_dir_name):
    os.makedirs(
        os.path.join(
            output,
            resource_dir_name,
        ),
    )


def save_resource(resource_content, output, filename):
    return None


def save_document(document, save_to):
    html_file_path = os.path.join(save_to, document.url)
    with open(html_file_path, mode=WB) as html_file:
        html_file.write(document.content)
