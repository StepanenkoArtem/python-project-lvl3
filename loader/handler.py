# coding=utf-8

"""Parse and handle downloaded HTML document."""

from urllib.parse import urlparse

BAR_CAPTION = 'Loading resources'
RESOURCE_TYPES = ('img', 'script', 'link')
RESOURCE_REFS = ('src', 'href')


def _is_resource(resource):
    """
    Figure out is the resource local (don't contain host in url).

    Args:
        resource : (class 'bs4.element.Tag')
            Object contains reference to resources (image, link or script).

    Returns:
        bool :
            Return True if resource object has reference without host,
            else return False
    """
    for attr in resource.attrs:
        if attr in {'src', 'href'}:
            url_parts = urlparse(resource.get(attr))
            scheme_n_netloc = url_parts.netloc or url_parts.scheme
            if len(url_parts.path) > 1 and not scheme_n_netloc:
                return True
    return False


def get_path(resource):
    """
    Obtain reference path to the local resource file.

    Args:
        resource : (class 'bs4.element.Tag')
            Object contains reference to resources (image, link or script).

    Returns:
        path : str
            String contains full path to resource file
            (excluding protocol and host)
    """
    for ref in RESOURCE_REFS:
        if resource.has_attr(ref):
            return resource.attrs[ref]


def update_resource(resource, new_link):
    """
    Update resource object reference to downloaded file.

    Args:
        resource : (class 'bs4.element.Tag')
            Object contains reference to resources (image, link or script).
        new_link : str
            New reference to downloaded resource file.

    Returns:
        resource : (class 'bs4.element.Tag')
            Updates resource object
    """
    for attr in RESOURCE_REFS:
        if resource.has_attr(attr):
            resource.attrs[attr] = new_link
    return resource


def get_resources(dom):
    """Update local resources on DOM.

    Args:
        dom : (bytes) html content

    Returns:
        : (list) list of resources
    """
    # Obtain list of local resources
    return list(filter(_is_resource, dom.find_all(RESOURCE_TYPES)))
