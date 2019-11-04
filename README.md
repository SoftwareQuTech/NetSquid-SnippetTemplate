How to create a NetSquid Snippet
================================

NetSquid snippets should follow the provided [template git repository](https://github.com/SoftwareQuTech/NetSquid-SnippetTemplate).
The template makes use of [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/index.html).

To instantiated a new folder for a new snippet, clone this repo, cd in to it and do

```shell
cookiecutter . -o /your/path
```

where `/your/path` is the folder you want to place the new snippet in. Note that you need `cookiecutter` installed which can be done by

```shell
pip3 install cookiecutter
```

You will then be asked to fill in a few things.
First you need to give it a name, for example of the form `NetSquid-SnippetName`.
If press `<enter>` on the two next entries, these will automatically become `netsquid-snippetname` (for the pip package name) and `netsquid_snippetname` for the folder containing the package.

These names and the other arguments will automatically be used in the new files created and there will already be test framework and docs setup for you to get started.
If you don't want to use the `cookiecutter` you can copy the folder `netsquid-mysnippet` in this repo and update the files manually following the conventions in the file `netsquid-mysnippet/HOWTO-SnippetTemplate`.
