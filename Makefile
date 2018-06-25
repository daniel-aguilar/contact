.PHONY: test isort lint

test: lint
	coverage run manage.py test --settings "settings.dev"

isort:
	isort -rc --atomic .

lint: isort
	flake8
