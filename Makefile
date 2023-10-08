install:
	@poetry install
	@poetry run pre-commit install -f -t pre-commit --hook-type commit-msg

shell:
	@poetry shell

run-python:
	@poetry run python

format:
	@poetry run black -l 80 . --exclude=.venv
	@poetry run flake8

check:
	@poetry run black -l 80 --check . --exclude=.venv

test:
	@PYTHONDONTWRITEBYTECODE=1 poetry run python3 -m unittest discover tests/ -v
