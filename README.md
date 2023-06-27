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

## 1. Prepare your copy of workshop repository
During the workshop we will use this repository to present GitHub Actions functionality. Please fork this repo to start workshop.

GitHub documentation: https://docs.github.com/en/get-started/quickstart/fork-a-repo

After forking the repository you may notice that Actions history is unavailable. First you have to enable Actions itself, after clicking
`Actions` tab. To create first workflow run please add another trigger to tha main workflow. Use `workflow_dispatch` trigger to make manual runs possible.
You have to push changes to main branch to make `workflow_dispatch` active

GitHub documentation: https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows

Please create manual workflow run

GitHub documentation: https://docs.github.com/en/actions/using-workflows/manually-running-a-workflow

## 2. Make main workflow green
As you may notice `report_jobs_results` job is failing after forking the repo. This is because missing actions secrets,
which are used for job execution. Please set secrets in `Settings` -> `Secrets and variables` -> `Actions` You need to specify two secrets:
`SPLUNK HOST`
`SPLUNK_TOKEN`

Values for those will be provided during the workshop

GitHub documentation: https://docs.github.com/en/actions/security-guides/encrypted-secrets

Examine logs from GitHub Actions console, try to use search box and rerun options

## 3. Create job running large tests
Create another job in main workflow, which runs large tests and name it `large-tests`. For now, it should run in parallel with
`small-tests` job. Make sure that results from GitHub Actions run are the same as local runs of large tests.

Modify needs parameter for `report_jobs_results`, as this job must be ran as the last one int the workflow.

GitHub documentation: https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idneeds

In context of `needs` parameter think about different job hierarchy in our project. You can also add `needs` to `pre-commit`, `small-tests`, `large-tests` jobs. What would be the best job dependency tree?

## 4. Adding artifacts
Modify your test jobs to create JUnit logs, store those logs as artifacts.

GitHub documentation: https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts
pytest documentation: https://docs.pytest.org/en/6.2.x/usage.html#creating-junitxml-format-files

Please notice that `large-tests` are failing and you need to add some logic because of this. By default, job stops execution after failed step

GitHub documentation: https://docs.pytest.org/en/6.2.x/usage.html#creating-junitxml-format-files
