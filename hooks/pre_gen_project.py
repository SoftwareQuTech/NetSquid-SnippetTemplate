import os


def apply_license(license):
    license_file = get_license_file(license)


def get_license_file(license):
    pass


license = "{{ cookiecutter.license }}"
print("Running before")
print(f"License is {license}")
print(f"cwd = {os.getcwd()}")
