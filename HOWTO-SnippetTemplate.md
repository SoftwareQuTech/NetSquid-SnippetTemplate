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

All NetSquid snippets should be offered as Python packages (or a single module) with the naming convention `netsquid_<snippetname>` e.g. `netsquid_trappedions` for a snippet offering support for trapped ion components.
Before naming your snippet please check on the [NetSquid snippets](https://netsquid.org/snippets) page that your name doesn't already exist.

The name of your snippet should follow the package name with the format `NetSquid-SnippetName` e.g. `NetSquid-TrappedIons`.
This is the name that should be used for the repository name, and on the [NetSquid snippets](https://netsquid.org/snippets) page.

Adapting the template
---------------------

The template repository contains the following files:

```
NetSquid-SnippetTemplate/    *RENAME*  - Git repository root directory
    netsquid_mypkg/          *RENAME*  - Python package directory
        __init__.py                    - Needed by package (keep this)
        example.py           *REPLACE* - Example module
        test_example.py      *REPLACE* - Example unit test
    setup.py                 *MODIFY*  - Setup script, including snippet meta data
    README.md                *MODIFY*  - Your snippet's README
    CHANGELOG.md             *MODIFY*  - Log of changes
    LICENSE                  *MODIFY*  - Your license
    INSTALL.md                         - General install instructions
    HOWTO-SnippetTemplate.md           - This file, can be removed
    LICENSE-SnippetTemplate            - License of this snippet (keep this)
    .git/...                           - Git repository
    .gitignore                         - What git should ignore, modify if needed
```

The files marked files need to be renamed, replaced or modified.
