install:
	poetry install

build:
	poetry build

publish:
	poetry publish -r testPyPI -u artem.stepanenko -p Fb_706428

lint:
	poetry run flake8 page_loader/

bump:
	poetry version patch

test:
	poetry run python -m pytest -vv

test-cov:
	poetry run python -m pytest -q --cov=page_loader tests/

test-cov2xml:
	poetry run python -m pytest --cov=page_loader tests/ --cov-report=xml
