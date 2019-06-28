How to create a NetSquid Snippet
================================

NetSquid snippets should follow the provided [template git repository](https://github.com/SoftwareQuTech/NetSquid-SnippetTemplate).
One way to do so is to clone this repository and use it as the base of your project:

```shell
git clone https://github.com/SoftwareQuTech/NetSquid-SnippetTemplate NetSquid-MySnippet
git remote rm origin
```

Alternatively, if you are using GitHub, you can also _fork_ the repository.
If your project already has a git repository, you can also simply copy over the files and adopt the required naming conventions.

Naming conventions
------------------

The name of your snippet should follow the naming convention `NetSquid-SnippetName` e.g. `NetSquid-TrappedIons` for a snippet offering support for trapped ion components.
This is the name that can be used for the repository and on the [NetSquid snippets](https://netsquid.org/snippets) webpage.

The Python _package name_, as specified in _setup.py_, should be all lower case i.e. `netsquid-snippetname`.
This is the name used to install the package or refer to it as a dependency.
For example, if the snippet is available on NetSquid's PyPi index server, it can be installed using:

```
pip3 install --user --extra-index-url https://<username>:<password>@pypi.netsquid.org netsquid-snippetname
```

The name of the package directory or module file should use an underscore in place of the dash i.e. `netsquid_snippetname/` or `netsquid_snippetname.py`.
The package can be imported in Python using this name:

```python
import netsquid_snippetname
```

Adapting the template
---------------------

The template repository contains the following files:

```
NetSquid-SnippetTemplate/    *RENAME*  - Git repository root directory
    netsquid_mysnippet/      *RENAME*  - Python package directory
        __init__.py                    - Needed by package (keep this)
        example.py           *REPLACE* - Example module
        test_example.py      *REPLACE* - Example unit test
    setup.py                 *MODIFY*  - Setup script, including snippet meta data
    README.md                *MODIFY*  - Your snippet's README
    CHANGELOG.md             *MODIFY*  - Log of changes
    LICENSE                  *MODIFY*  - Your license
    requirements.txt         *MODIFY*  - Python package requirements
    INSTALL.md                         - General install instructions
    HOWTO-SnippetTemplate.md           - This file, can be removed
    LICENSE-SnippetTemplate            - License of this snippet (keep this)
    Makefile                           - Specifying make commands, i.e. make tests (keep this)
    .flake8                            - Specifying linting rules (keep this)
    .git/...                           - Git repository
    .gitignore                         - What git should ignore, modify if needed
```

The files marked files need to be renamed, replaced or modified.
