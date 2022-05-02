# Included so pytest can be run on github actions. Test will fail without this file.
# In order to pass pytest (and pylint) on Github Actions,
# where my files are structured as below,
# I had to add an __init__.py inside the tests directory.
# Documentation on it: https://docs.pytest.org/en/latest/explanation/pythonpath.html#pythonpath
#
##############################################
# Project Package Structure 4/22/2022
##############################################
# .
# ├── project-proposal.md
# ├── readme.md
# └── src/
#     ├── example_model.py
#     ├── find_pyomo_constraints.py
#     ├── __init__.py
#     ├── LICENSE
#     ├── readme.md
#     ├── setup.py
#     └── tests/
#         ├── __init__.py
#         └── project_test.py
#
#
# Workflows that FAIL if __init__.py file NOT inside tests/
#     passes_pylint:
#         runs-on: ubuntu-latest
#         steps:
#         - uses: actions/checkout@v3
#         - run: |
#                 pip install pylint
#                 pip install pyomo
#                 pylint ./src/find_pyomo_constraints.py (PASSES)
#                 pylint ./src/tests/project_test.py (FAILS with import error)
#
#     passes_pytest:
#         runs-on: ubuntu-latest
#         steps:
#         - uses: actions/checkout@v3
#         - run: |
#                 pip install pytest
#                 pip install pyomo
#                 pytest (FAILS with import error)
