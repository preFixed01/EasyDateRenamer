.ONESHELL:
ENV_PREFIX=$(shell python -c "if __import__('pathlib').Path('.venv/bin/pip').exists(): print('.venv/bin/')")

.PHONY: help
help:             ## Show the help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep


.PHONY: show
show:             ## Show the current environment.
	@echo "Current environment:"
	@echo "Running using $(ENV_PREFIX)"
	@$(ENV_PREFIX)python -V
	@$(ENV_PREFIX)python -m site

.PHONY: install
install:          ## Install the project in dev mode.
	@echo "Don't forget to run 'make virtualenv' if you got errors."
	$(ENV_PREFIX)pip install -e .[test]

.PHONY: fmt
fmt:              ## Format code using black & isort.
	$(ENV_PREFIX)isort easy_date_renamer/
	$(ENV_PREFIX)black easy_date_renamer/
	$(ENV_PREFIX)black tests/

.PHONY: lint
lint:             ## Run pep8, black, mypy linters.
	$(ENV_PREFIX)flake8 --config pyproject.toml easy_date_renamer/
	$(ENV_PREFIX)pylint easy_date_renamer/
	$(ENV_PREFIX)black --check easy_date_renamer/
	$(ENV_PREFIX)black --check tests/
	$(ENV_PREFIX)mypy easy_date_renamer

.PHONY: test
test: lint        ## Run tests and generate coverage report.
	$(ENV_PREFIX)pytest -v --cov=easy_date_renamer -l --tb=short --maxfail=1 tests/ --junitxml=report.xml
	$(ENV_PREFIX)pytest --cov --cov-report term --cov-report xml:coverage.xml

.PHONY: watch
watch:            ## Run tests on every change.
	ls **/**.py | entr $(ENV_PREFIX)pytest -s -vvv -l --tb=long --maxfail=1 tests/

.PHONY: clean
clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf .coverage
	@rm -rf coverage.xml
	@rm -rf .tox/
	@rm -rf docs/_build
	@rm -rf public
	@rm -rf report.xml

.PHONY: virtualenv
virtualenv:       ## Create a virtual environment.
	@echo "creating virtualenv ..."
	@rm -rf .venv
	@python3 -m venv .venv
	@./.venv/bin/pip install -U pip
	@./.venv/bin/pip install -e .[test]
	@echo
	@echo "!!! Please run 'source .venv/bin/activate' to enable the environment !!!"

.PHONY: docs
docs:             ## Build the documentation.
	@echo "building documentation ..."
	@$(ENV_PREFIX)mkdocs build
