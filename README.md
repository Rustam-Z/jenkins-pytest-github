# jenkins-pytest-github
Jenkins CI pipeline integrated with the GitHub Webhook. In any push action on GitHub, auto tests will be running by Jenkins, and coverage report will be generated.

## Project structure
- `tests/test_calc_func.py` - contains math functions
- `tests/test_calc_class.py` - contains a basic Calculator class 

Test modules are placed under the `tests` directory. Note that tests is not a Python package and has no "__init__.py" file.

It is also possible to run pytest directly with the "pytest" or "py.test" command, instead of using the longer "python -m pytest" module form. However, the shorter command does not append the current directory path to PYTHONPATH.

## How to run?
- `pip install -r requirements.txt`
- `python -m pytest -v --tb=no`
- `python -m pytest --junitxml=results.xml`
- `python -m pytest --cov=src` to see the coverage
- `python -m pytest --cov=src --cov-report=html`