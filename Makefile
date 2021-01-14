install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --user dist/*.whl

lint:
	poetry run flake8 --ignore=E712,E711 gendiff

test:
	poetry run pytest --cov=gendiff/tests --cov-report xml
