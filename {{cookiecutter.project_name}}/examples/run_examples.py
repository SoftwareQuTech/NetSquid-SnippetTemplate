import os
import runpy
import inspect

# This file is used to run all the examples in this folder and subfolders
# Each file should be of the form example*.py and contain a `main`-method.
# If the `main`-method takes an argument `no_output` this will be passed as `True`
# to avoid creating plots etc.


def main():
    path_to_here = os.path.dirname(os.path.abspath(__file__))
    for root, folders, files in os.walk(path_to_here):
        for filename in files:
            if filename.startswith("example") and filename.endswith(".py"):
                filepath = os.path.join(root, filename)
                _run_example(filepath)


def _run_example(filepath):
    namespace = runpy.run_path(filepath)
    if "main" in namespace:
        main = namespace["main"]
    else:
        return

    if _has_no_output_arg(main):
        main(no_output=True)
    else:
        main()


def _has_no_output_arg(func):
    return "no_output" in inspect.getfullargspec(func).args


if __name__ == '__main__':
    main()
