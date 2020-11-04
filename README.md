# pload

[![Build Status](https://github.com/StepanenkoArtem/python-project-lvl3/workflows/Build/badge.svg)](https://github.com/StepanenkoArtem/python-project-lvl3/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/0c5f98e70a04ca23c02c/maintainability)](https://codeclimate.com/github/StepanenkoArtem/python-project-lvl3/maintainability)
[![Test Coverage](https://codecov.io/gh/StepanenkoArtem/python-project-lvl3/branch/master/graph/badge.svg)](https://codecov.io/gh/StepanenkoArtem/python-project-lvl3)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

This CLI programm downloading remote web-pages to specified folder on your local machines.
Downloading URLs should be specified as command-line argument.

## Installation

Run next command for installing page-loader package

    pip install --extra-index-url https://pypi.org/simple -i https://test.pypi.org/simple pload

[![asciicast](https://asciinema.org/a/WKFA9AqAUVolWh0PvYITrQnLa.svg)](https://asciinema.org/a/WKFA9AqAUVolWh0PvYITrQnLa)

## Usage

1. Common usage format.

        pload [OPTIONS] URL

    For downloading web page run `pload` with specified url as argument.

        pload https://www.wikipedia.org/

    [![asciicast](https://asciinema.org/a/FA3pI2erJPHJestriE6dj7F3R.svg)](https://asciinema.org/a/FA3pI2erJPHJestriE6dj7F3R)

    By default downloaded documents will save to subdirectory `downloads` in current workind directory.

2. Options

    `--help`

    To get help info

    [![asciicast](https://asciinema.org/a/WKFA9AqAUVolWh0PvYITrQnLa.svg)](https://asciinema.org/a/WKFA9AqAUVolWh0PvYITrQnLa)

        `--output`
    Specify directory for saving files.

    [![asciicast](https://asciinema.org/a/onbK40nDRnpwxUcsUBIXxmx5p.svg)](https://asciinema.org/a/onbK40nDRnpwxUcsUBIXxmx5p)

        `--logfile`
    Specify custom logging file.

    [![asciicast](https://asciinema.org/a/ckDtZzxNTPqNbuQuxOuDwX6BE.svg)](https://asciinema.org/a/ckDtZzxNTPqNbuQuxOuDwX6BE)

        `--loglevel`

    Set logging level. There are five valid options available: 'DEBUG', 'INFO', 'WARNING', 'ERROR' and 'CRITICAL'. Both small and upper register is allowable. Integer value also acceptable: 10, 20, 30, 40, 50 accordingly.

   [![asciicast](https://asciinema.org/a/SxqsHzictc4T2ZFQwOJ0Wb6uy.svg)](https://asciinema.org/a/SxqsHzictc4T2ZFQwOJ0Wb6uy)
