from page_loader.scripts.loader import main
from page_loader.scripts.loader import t



def main_test():
    assert main() == 'This is the test'

def test_t():
    assert t() == None
