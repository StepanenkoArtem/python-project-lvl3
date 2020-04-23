import os

# File operations modes
WB = 'wb'


def create_output_dir(output):
    if not os.path.exists(output):
        os.makedirs(output)


def create_resource_dir(output, resource_dir_name):
    os.makedirs(
        os.path.join(
            output,
            resource_dir_name,
        ),
    )


def save_document(document_content, path, filename):
    fullpath = os.path.join(path, filename)
    with open(fullpath, mode=WB) as html_file:
        html_file.write(document_content)
