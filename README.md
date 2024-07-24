## JFrog sample project

This is a sample python project demonstrating how to publish a module to Artifactory.

## Configuration

To resolve packages from Artifactory using pip, add the following to ~/.pip/pip.conf:
```
[global]
index-url = https://<Artifactory-url>/artifactory/api/pypi/<PyPI-Repository>/simple
local/simple
```

## Installation

Run the following commands to build & publish your module:
1. ```pip install twine```
2. ```python -m build --sdist``` or ```python setup.py sdist```
3. ```twine upload --repository-url https://example.jfrog.io/artifactory/api/pypi/hello-pypi  dist/* -u<USER> -p<TOKEN>```
