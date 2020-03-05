from page_loader import helpers, parser
from page_loader.download import download


def save_html(downloaded, output_dir):
    modified_html = parser.localize_resources(
        html=downloaded.content,
        resource_dir=helpers.get_resource_dir_name(downloaded.url),
    )
    html_file_path = helpers.get_html_file_path(downloaded.url, output_dir)
    with open(html_file_path, 'bw') as html_file:
        html_file.write(modified_html)
        return True


def save_resources(downloaded, output_dir):
    resources = parser.get_local_resources(downloaded.content)
    if resources:
        helpers.create_resource_dir(downloaded.url, output_dir)
        for resource in resources:
            resource_url = downloaded.url + resource
            resource_file_path = helpers.get_resource_file_path(resource)
            with open(resource_file_path) as resource_file:
                resource_file.write(download(resource_url).content)


def save(dowloaded, save_to):
    output_dir = helpers.get_full_path(save_to)
    save_html(dowloaded, output_dir)
    save_resources(dowloaded, output_dir)
