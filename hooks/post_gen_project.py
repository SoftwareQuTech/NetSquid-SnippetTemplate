import os

license = "{{ cookiecutter.license }}"
print("Running after")
print(f"License is {license}")
print(f"cwd = {os.getcwd()}")
