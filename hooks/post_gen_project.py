import os
import shutil


def apply_license(license):
    license_file = get_license_file(license)
    license_folder = ".licenses"

    # Copy the chosen license file to root
    shutil.copy(os.path.join(license_folder, license_file), "LICENSE")

    # Remove the license folder
    shutil.rmtree(license_folder)


def get_license_file(license):
    license_files = {
        "Apache-2.0": "APACHE_LICENSE",
        "MIT": "MIT_LICENSE",
        "BSD-3": "BSD_LICENSE",
        "GNU GPL v3.0": "GNU_LICENSE",
    }

    if license not in license_files:
        raise ValueError(f"Unknown license {license}")
    return license_files[license]


license = "{{ cookiecutter.license }}"
apply_license(license)
