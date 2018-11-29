# Edit the setup parameters below to match your snippet
#
from setuptools import setup, find_packages
from os import path


def load_readme_text():
    # Load in README file as a string
    try:
        dir_path = path.abspath(path.dirname(__file__))
        with open(path.join(dir_path, 'README.md'), encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""


setup(
    name='NetSquid-MySnippet',
    version='1.0.0',
    url='http://github.com/joebloggs/netsquid-mysnippet/',
    author='<your name>',
    author_email='<your email>',
    description='<description of your snippet>',
    long_description=load_readme_text(),
    long_description_content_type='text/markdown',
    license='Apache-2.0',
    python_requires='>=3.5',
    packages=find_packages(),
    #py_modules=['netsquid_mysnippet'],  # if offering a single module file
    install_requires=[
        'netsquid'  # any version
        #'netsquid>=0.3.5'  # require a minimum version
        #'netsquid=0.3.5'  # require a specific version
    ],
    test_suite='netsquid_mysnippet',
    zip_safe=False,
    include_package_data=True,
    platforms='any',
)
