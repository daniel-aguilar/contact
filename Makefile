.PHONY: test lint format

test: lint
	coverage run manage.py test --settings "contact.settings.dev"

lint: format
	ruff check

format:
	ruff format --check
