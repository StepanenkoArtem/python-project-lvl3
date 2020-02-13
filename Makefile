install:
	poetry install

build:
	poetry build

publish:
	poetry publish -r testPyPI -u artem.stepanenko -p Fb_706428

lint:
	poetry run flake8 gendiff.py

bump:
	poetry version patch

test:
	poetry run python -m pytest -vv

cov-test:
	poetry run python -m pytest --cov=page_loader tests/

cov_test2xml:
	poetry run python -m pytest --cov=page_loader tests/ --cov-report=xml
