# github-ci-presentation
Repository to present GitHub Actions on PyCon PL 2023

# Requirements
Poetry >= 1.3.0 [installation guide](https://python-poetry.org/docs/#installing-with-the-official-installer)
Python >= 3.7
git
GitHub account

PyPI account (optional)

# Setup
Clone github-ci-presentation repository:
```
git clone git@github.com:uoboda-splunk/github-ci-presentation.git
```
Install project
```
poetry install
```
Spawn a poetry shell
```
poetry shell
```

# Tasks

## 1. Create job running large tests
Create another job in main workflow, which runs large tests and name it `large-tests`. For now it should run in parallel with
`small-tests` job