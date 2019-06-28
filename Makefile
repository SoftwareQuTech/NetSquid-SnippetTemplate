PYTHON3 = python3

python-deps:
	@$(PYTHON3) -m pip install --user -r requirements.txt

clean:
	@/usr/bin/find . -name '*.pyc' -delete

lint:
	@$(PYTHON3) setup.py flake8

tests:
	@$(PYTHON3) setup.py test

verify: clean python-deps lint tests

.PHONY: clean lint python-deps tests verify
