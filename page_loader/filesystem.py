import os

# File operation modes
WRITE = 'w'


def create_dir(output):
    """
    Create destination directory.

    Args:
        output (str): Path for directory

    Returns:
        (Boolean): Returns path if directory created successfully,
        esle returns False

    """
    if not os.path.exists(output):
        os.makedirs(output)
        return (output)
    return False


def save_document(document_content, path_file):  # noqa: D103
    with open(path_file, mode=WRITE) as html_file:
        html_file.write(document_content)
