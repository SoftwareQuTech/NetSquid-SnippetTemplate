from setuptools import setup, find_packages, Command
import os
from os import path
import re
import subprocess
import configparser

# Get config parameters
config = configparser.ConfigParser()
config.read('setup.cfg')
pkg_name = config['metadata']['name']
pypi_server = config['netsquid']['pypi-server']


def load_readme_text():
    """Load in README file as a string."""
    try:
        dir_path = path.abspath(path.dirname(__file__))
        with open(path.join(dir_path, 'README.md'), encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""


def load_requirements():
    """Load in requirements.txt as a list of strings."""
    try:
        dir_path = path.abspath(path.dirname(__file__))
        with open(path.join(dir_path, 'requirements.txt'), encoding='utf-8') as f:
            install_requires = [line.strip() for line in f.readlines()]
            return install_requires
    except FileNotFoundError:
        return ""


class DeployCommand(Command):
    """Run command for uploading binary wheel files to NetSquid PyPi index.

    """
    description = "Deploy binary wheel files to NetSquid PyPi index."
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def _get_gitbranch(self):
        # Get name of current git branch
        output = subprocess.run(('git', 'symbolic-ref', 'HEAD'), capture_output=True, encoding='utf8').stdout
        return re.sub('refs/heads/', '', output.rstrip())

    def run(self):
        print("Uploading binary snippet {} wheels to {} (requires authentication)"
              .format(pkg_name, pypi_server))
        if self._get_gitbranch() != 'master':
            print("ERROR: Attempting to upload from a branch different than master.")
            return
        if 'NETSQUIDCI_USER' not in os.environ:
            print("ERROR: environment variable NETSQUIDCI_USER is not defined.")
            return
        # Create package directory if needed
        subprocess.run(("/usr/bin/ssh", "{}@{}".format(os.environ['NETSQUIDCI_USER'], pypi_server),
                        "mkdir", "-p", "/srv/netsquid/pypi/{}".format(pkg_name)),
                       capture_output=True, encoding='utf8').check_returncode()
        # Check for wheel files
        wheel_files = []
        for f in os.listdir("dist/"):
            if f.endswith(".whl"):
                wheel_files.append("dist/{}".format(f))
        # Upload wheel files
        if len(wheel_files) > 0:
            subprocess.run(("/usr/bin/scp", " ".join(wheel_files), "{}@{}:/srv/netsquid/pypi/{}/".format(
                os.environ['NETSQUIDCI_USER'], pypi_server, pkg_name)), capture_output=True, encoding='utf8').check_returncode()
        else:
            print("ERROR: no wheel files in dist/ to upload.")


setup(
    cmdclass={"deploy": DeployCommand},
    long_description=load_readme_text(),
    long_description_content_type='text/markdown',
    python_requires='>=3.5',
    packages=find_packages(),  # if offering a package
    #py_modules=['pkgname.replace('-', '_')'],  # if offering a single module file
    install_requires=load_requirements(),
    test_suite=pkg_name.replace('-', '_'),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
)
