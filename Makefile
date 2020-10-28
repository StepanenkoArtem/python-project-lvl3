install:
	poetry install

build:
	poetry build

publish:
	poetry publish -r testPyPI -u $(user) -p $(password)

lint:
	poetry run flake8 loader/

bump:
	poetry version patch

test:
	poetry run python -m pytest -vv --ff

test-cov:
	poetry run python -m pytest -q --cov=loader tests/

coverage: coverage.xml
	poetry run python -m pytest --cov=loader tests/ --cov-report=xml

.PHONY:
	build
	install
	publish
	lint
	bump
	test
	test-cov
	coverage