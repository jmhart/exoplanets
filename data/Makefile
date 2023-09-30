
.PHONY: help
help: # Show the help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "#" Makefile | fgrep -v fgrep

.PHONY: show
show: # Show the current environment.
	@echo "Current environment:"
	@pipenv run python -V

.PHONY: init
init: # Install dependencies and spawn virtualenv shell.
	@pipenv shell
	@pipenv install

.PHONY: fmt
fmt: # Format code using black & isort.
	@pipenv run isort src/
	@pipenv run black src/
	@pipenv run black test/

.PHONY: lint
lint: # Run black, mypy linters.
	@pipenv run black --check src/
	@pipenv run black --check test/
	@pipenv run mypy --ignore-missing-imports src/

.PHONY: test
test: lint # Run tests and generate coverage report.
	@pipenv run python -m pytest -v --maxfail=1 --cov --cov-branch --cov-fail-under=100 test/
	@pipenv run coverage xml
	@pipenv run coverage html

.PHONY: clean
clean: # Clean unused files.
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build

.PHONY: docs
docs: # Build the documentation.
	@echo "building documentation ..."
	@pipenv run mkdocs build
