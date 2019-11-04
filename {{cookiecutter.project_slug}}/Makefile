PYTHON3      = python3
SOURCEDIR    = {{ cookiecutter.project_folder }}
TESTDIR      = tests
EXAMPLES     = examples
RUNEXAMPLES  = ${EXAMPLES}/run_examples.py
MINCOV       = {{ cookiecutter.minimum_coverage }}

help:
	@echo "install           Installs the package (editable)."
	@echo "verify            Verifies the installation, runs the linter and tests."
	@echo "test              Runs the tests."
	@echo "examples          Runs the examples and makes sure they work."
	@echo "open-cov-report   Creates and opens the coverage report."
	@echo "lint              Runs the linter."
	@echo "deploy-bdist      Builds and uploads the package to the netsquid pypi server."
	@echo "bdist             Builds the package."
	@echo "test-deps         Installs the requirements needed for running tests and linter."
	@echo "python-deps       Installs the requirements needed for using the package."
	@echo "clean             Removes all .pyc files."
	

test-deps:
	@$(PYTHON3) -m pip install -r test_requirements.txt

python-deps:
	@$(PYTHON3) -m pip install -r requirements.txt

clean:
	@/usr/bin/find . -name '*.pyc' -delete

lint:
	@$(PYTHON3) -m flake8 ${SOURCEDIR} ${TESTDIR} ${EXAMPLEDIR}

tests:
	@$(PYTHON3) -m pytest --cov=${SOURCEDIR} --cov-fail-under=${MINCOV} tests

open-cov-report:
	@$(PYTHON3) -m pytest --cov=${SOURCEDIR} --cov-report html tests && open htmlcov/index.html

examples:
	@${PYTHON3} ${RUNEXAMPLES} > /dev/null && echo "Examples OK!" || echo "Examples failed!"

bdist:
	$(PYTHON3) setup.py bdist_wheel

install: test-deps
	@$(PYTHON3) -m pip install -e .

_clean_dist:
	/bin/rm -rf dist

deploy-bdist: _clean_dist bdist
	$(PYTHON3) setup.py deploy

verify: clean test-deps python-deps lint tests examples _verified

_verified:
	@echo "The snippet is verified :)"

.PHONY: clean lint test-deps python-deps tests verify bdist deploy-bdist _clean_dist install open-cov-report examples
