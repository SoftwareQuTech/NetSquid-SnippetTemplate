PYTHON        = python3
PIP           = pip3

python-deps:
	@$(PIP) install -r requirements.txt

clean:
	@find . -name '*.pyc' -delete

lint:
	@$(PYTHON) setup.py flake8

tests:
	@$(PYTHON) setup.py test

verify: clean python-deps lint tests

.PHONY: clean lint python-deps tests verify
