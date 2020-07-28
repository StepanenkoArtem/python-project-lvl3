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

[![asciicast](https://asciinema.org/a/CQyUMCvHSGBQg9T0nT9mEoAKy.svg)](https://asciinema.org/a/CQyUMCvHSGBQg9T0nT9mEoAKy)

## Usage

1. Common usage format.
    stepanenko-page-loader [OPTIONS] URL

2. Run
    stepanenko-page-loader --help
to get short help

3. To download web page run next
    stepanenko-page-loader URL

For example, if you want to download `https://
