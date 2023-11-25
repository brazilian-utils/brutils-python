install:
	@poetry install

shell:
	@poetry shell

run-python:
	@poetry run python

format:
	@poetry run ruff format .
	@poetry run ruff check . --fix

check:
	@poetry run ruff format . --check
	@poetry run ruff .

test:
	@PYTHONDONTWRITEBYTECODE=1 poetry run python3 -m unittest discover tests/ -v
