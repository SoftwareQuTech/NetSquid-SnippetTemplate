PYTHON         = python3
PIP            = pip3
PYPI_SERVER    = pypi.netsquid.org
GITBRANCH_NAME = $(shell git symbolic-ref HEAD | sed -e 's,.*/\(.*\),\1,')
SNIPPET_NAME   = $(shell basename $(PWD))
PACKAGE_NAME   = $(shell echo $(SNIPPET_NAME) | tr A-Z a-z)

python-deps:
	@$(PIP) install -r requirements.txt

clean:
	@find . -name '*.pyc' -delete

lint:
	@$(PYTHON) setup.py flake8

tests:
	@$(PYTHON) setup.py test

bdist:
	@echo -e "\n*** Create a binary $(SNIPPET_NAME) wheel distribution file"
	$(PYTHON) setup.py bdist_wheel

deploy-bdist: bdist
	@echo -e "\n*** Uploading binary snippet $(SNIPPET_NAME) wheels to $(PYPI_SERVER) (requires authentication)"
ifneq ($(shell echo $(GITBRANCH_NAME)), master)
	@echo -e "ERROR: attempting to upload from a branch different than master."
	exit 1
endif
ifdef NETSQUIDCI_USER
	/usr/bin/ssh "$(NETSQUIDCI_USER)@$(PYPI_SERVER)" "mkdir /srv/netsquid/pypi/$(PACKAGE_NAME)" 2> /dev/null || true
	/usr/bin/scp dist/*.whl "$(NETSQUIDCI_USER)@$(PYPI_SERVER):/srv/netsquid/pypi/$(PACKAGE_NAME)/"
else
	@echo -e "ERROR: environment variable NETSQUIDCI_USER is not defined."
	exit 1
endif

verify: clean python-deps lint tests

.PHONY: clean lint python-deps tests verify bdist deploy-bdist
