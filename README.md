How to create a NetSquid Snippet
================================

NetSquid snippets should follow the provided [template git repository](https://github.com/SoftwareQuTech/NetSquid-SnippetTemplate).
The template makes use of [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/index.html).
You can install cookiecutter as
```shell
pip3 install cookiecutter
```
See the [docs](https://cookiecutter.readthedocs.io/en/latest/installation.html) for more instructions.

To see other snippets and to access netsquid itself, see https://netsquid.org/.

To instantiated a new folder for a new snippet, clone this repo, cd in to it and do

```shell
./make.sh . -o /your/path
```

where `/your/path` is the folder you where your snippet will be placed (note that this is not the snippet project directory itself.

You will then be asked to fill in a few things.
First you need to give it a name, for example of the form `NetSquid-SnippetName`.
If press `<enter>` on the two next entries, these will automatically become `netsquid-snippetname` (for the pip package name) and `netsquid_snippetname` for the folder containing the package.

These names and the other arguments will automatically be used in the new files created and there will already be test framework and docs setup for you to get started.

The cookiecutter will create the files below.
The files marked by (replace) are dummy files that should be replaced with your actual package and tests etc.

```
NetSquid-SnippetTemplate/            - Git repository root directory
    netsquid_mysnippet/              - Python package directory
        __init__.py                  - Needed by package
        samplemodule.py              - Example module (replace)
    docs/                            - Folder containing docs
        modules/                     - Folder for autodoc of doc-strings
            samplemodule.rst         - Example module for autodoc (replace)
        README.md                    - README for how to build the docs
        Makefile                     - Specifying the make commands for building the docs (`make build`)
        requirements.txt             - Requirements for building the docs
        conf.py                      - Configuration of the docs
        index.rst                    - Entrypoint of the docs
        installation.rst             - Installation instructions in the docs
        usage.rst                    - Usage instructions in the docs
        api.rst                      - API documentation
        make.bat                     - For running make on windows
    tests/                           - Folder containing tests
        test_samplemodule.py         - Example test (replace)
    examples/                        - Folder containing examples
        run_examples.py              - Script to run all examples
        examples_samplemodule.py     - Example example (replace)
    setup.cfg                        - Configuration for setup script
    README.md                        - Your snippet's README
    CHANGELOG.md                     - Log of changes
    LICENSE                          - Your license
    requirements.txt                 - Python package requirements
    test_requirements.txt            - Requirements for running tests and linter
    setup.py                         - Setup script
    INSTALL.md                       - General install instructions
    HOWTO-SnippetTemplate.md         - This file, can be removed
    LICENSE-SnippetTemplate          - License of this snippet
    Makefile                         - Specifying make commands, i.e. make tests
    .bumpversion.cfg                 - Bumpversion configuration for versioning
    .flake8                          - Specifying linting rules
    .gitignore                       - What git should ignore, modify if needed
    .gitlab-ci.yml                   - Specifying CI on gitlab
    .coveragerc                      - Specifying how to compute test coverage
```
