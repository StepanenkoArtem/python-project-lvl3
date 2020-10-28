#!/usr/bin/env python
# coding=utf-8

"""Main module."""

import logging
import sys

from loader import network, storage
from loader.cli import main

if __name__ == '__main__':
    try:
        main()
    except ValueError:
        logging.error()
        sys.exit(3)
    except network.NetworkError as network_err:
        logging.error(network_err)
        logging.debug(network_err.__cause__)
        sys.exit(network_err.exit_code)
    except storage.StorageError as storage_err:
        logging.error(storage_err)
        logging.debug(storage_err.__cause__)
        sys.exit(storage_err.exit_code)
