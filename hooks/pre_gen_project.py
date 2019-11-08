snippet_name = "{{ cookiecutter.snippet_name }}"
project_name = "{{ cookiecutter.project_name }}"
project_slug = "{{ cookiecutter.project_slug }}"
project_folder = "{{ cookiecutter.project_folder }}"


def assert_snippet_name(snippet_name):
    if "netsquid" in snippet_name.lower():
        raise ValueError("snippet_name should not contain 'NetSquid'")


def assert_name(variable_name, variable, should_start_with):
    if not variable.startswith(should_start_with):
        raise ValueError(f"{variable_name} should start with '{should_start_with}', not {variable}")


assert_snippet_name(snippet_name)
variable_names = [f"project_{name}" for name in ["name", "slug", "folder"]]
names = [project_name, project_slug, project_folder]
should_start_withs = ["NetSquid-", "netsquid-", "netsquid_"]
for vname, v, sswith in zip(variable_names, names, should_start_withs):
    assert_name(vname, v, sswith)
