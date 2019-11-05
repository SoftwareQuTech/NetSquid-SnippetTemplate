# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = .
BUILDDIR      = build
PROJECTNAME   = {{ cookiecutter.project_slug }}
DOCSSERVER    = pypi.netsquid.org
DOCSFOLDER    = /srv/netsquid/docs/snippets

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


python-deps:
	pip3 install -r requirements.txt

build: python-deps html

open:
	open ${BUILDDIR}/html/index.html

see: html open

upload:
ifdef NETSQUIDCI_USER
	echo "scp -r ${BUILDDIR}/html/* $NETSQUIDCI_USER@${DOCSSERVER}:${DOCSFOLDER}/${PROJECTNAME}"
else
	$(error Set the environment variable NETSQUIDCI_USER before uploading)
endif

.PHONY: help Makefile python-deps build open see
