# PAGE Loader

[![Build Status](https://github.com/StepanenkoArtem/python-project-lvl3/workflows/Build/badge.svg)](https://github.com/StepanenkoArtem/python-project-lvl3/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/0c5f98e70a04ca23c02c/maintainability)](https://codeclimate.com/github/StepanenkoArtem/python-project-lvl3/maintainability)
[![Test Coverage](https://codecov.io/gh/StepanenkoArtem/python-project-lvl3/branch/master/graph/badge.svg)](https://codecov.io/gh/StepanenkoArtem/python-project-lvl3)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

This CLI programm downloading remote web-pages to specified folder on your local machines.
Downloading URLs should be specified as command-line argument.

## Installation

Run next command for installing page-loader package

    pip install --extra-index-url https://pypi.org/simple -i https://test.pypi.org/simple stepanenko-page-loader

[![asciicast](https://asciinema.org/a/icIdAGzhTZC5VTgd7ozrfoUow.svg)](https://asciinema.org/a/icIdAGzhTZC5VTgd7ozrfoUow)

## Usage

ol 1. Common usage format.

    stepanenko-page-loader [OPTIONS] URL

For downloading web page run `stepanenko-page-loader` with specified url as argument.

    stepanenko-page-loader nytimes.com

[![asciicast](https://asciinema.org/a/EIBtD72GWWeFbjueid5vNRf99.svg)](https://asciinema.org/a/EIBtD72GWWeFbjueid5vNRf99)

By default downloaded documents will save to subdirectory `spl-downloads` in current workind directory.

ol 2. Options

    `--help` - To get help info

[![asciicast](https://asciinema.org/a/fGw6BmDu2GV6Q3NJbYQGwlG1i.svg)](https://asciinema.org/a/fGw6BmDu2GV6Q3NJbYQGwlG1i)

    `--output` - Specify directory for saving files.

[![asciicast](https://asciinema.org/a/LzIR8SY1pxR9g7AjE9xLiBAp0.svg)](https://asciinema.org/a/LzIR8SY1pxR9g7AjE9xLiBAp0)

    `--logfile` - Specify custom logging file. 

[![asciicast](https://asciinema.org/a/ZGA8kbeVLvj5eHKu86tXpBuTf.svg)](https://asciinema.org/a/ZGA8kbeVLvj5eHKu86tXpBuTf)

    `--loglevel` - Set logging level. There are five valid options available: 'DEBUG', 'INFO', 'WARNING', 'ERROR' and 'CRITICAL'. Both small and upper register is allowable. Integer value also acceptable: 10, 20, 30, 40, 50 accordingly.
