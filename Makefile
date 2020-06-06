.PHONY: test lint isort

test:
	coverage run manage.py test --settings "settings.dev"

lint: isort
	flake8

isort:
	isort -c
