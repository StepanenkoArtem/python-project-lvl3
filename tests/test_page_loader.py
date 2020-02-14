from page_loader.scripts.loader import main, t


def main_test():
    assert main() == 'This is the test'


def test_t():
    assert t() == None
