install:
	poetry install

check:
	poetry check

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --user dist/*.whl

lint:
	poetry run flake8 --ignore=E712,E711 gendiff

test:
	poetry run pytest --cov=gendiff/tests -vv --cov-report xml

.PHONY: install test lint check build
