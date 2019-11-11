#!/usr/bin/env bash

# Make sure cookiecutter is installed
if !(hash cookiecutter 2> /dev/null); then
    echo "You need to have the python package 'cookiecutter' installed"
    echo "and the binary in you path."
    echo "To install this do 'pip3 install cookiecutter' and check that"
    echo "'cookiecutter --version' works."
    echo ""
    exit 1
fi

# Check if there are any arguments
if [ $# -eq 0 ]; then
    echo "To create a new instance of the template you need to provide"
    echo "a path to the template (this folder) and optionally where you"
    echo "want to put the new instance."
    echo "For example do './make.sh . -o ~/output/dir'."
    exit 1
fi

# Print some information
echo "You will now be asked a for a number of arguments to give to the new"
echo "instance of the template."
echo ""
echo "For each argument you can either enter your choice of press <Enter>"
echo "to use the defult in (in [])."
echo ""
echo "For the first argument you should provide a descriptive name of your snippet,"
echo "which will be prepended with 'NetSquid-'."
echo "For example, if you're making a snippet for simulating ion traps, you can"
echo "(for the argument 'snippet_name') for example enter 'IonTraps'."
echo "You should then use the default choice for the next three arguments, which will be:"
echo "\"project_name\":    NetSquid-IonTraps   (used in e.g. README.md)"
echo "\"project_slug\":    netsquid-iontraps   (this will be the python package name)"
echo "\"project_folder\":  netsquid_iontraps   (name of the source-code folder)"
echo ""
echo "The other arguments are:"
echo "\"description\":         A one-line description of the package."
echo "\"author_name\":         Your name of organization."
echo "\"author_email\":        A contact email."
echo "\"version\":             The version you want to start with."
echo "\"license\":             Chose one of the license options (will create the correct LICENSE file"
echo "\"copyright\":           Year and name for of copyright."
echo "\"url\":                 URL of the package, i.e. github/gitlab repo."
echo "\"docs_server\":         Where to upload the docs."
echo "\"pip_server\":          Where to upload the package wheel."
echo "\"netsquid_constraint\": Which netsquid is required."
echo "\"minimum coverage\":    What minimum test coverage should be enforced."
echo ""

cookiecutter "$@"
