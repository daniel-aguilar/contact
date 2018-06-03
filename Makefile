.PHONY: coverage test isort lint

coverage: test
	coverage report

test: lint
	coverage run manage.py test --settings "interaction.settings.dev"

isort:
	isort -rc --atomic .

lint: isort
	flake8
