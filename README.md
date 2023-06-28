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

# Project description
jobsim library is designed to be a simple workplace manager. For now it allows to register new employees and schedule introduction trainings for them. Different departments and locations can be defined in jobsim\departments and jobsim\locations directories respectively. After assigning the employee to its deaprtment and location trainings can be scheduled.

The example.py file in jobsim repo contains an example how the library can be used

```python
from jobsim.employee import Employee
from jobsim.location import Location
from jobsim.department import Department
from jobsim.trainings_scheduler import schedule_trainings

IT = "it"
FINANCE = "finance"
SF = "San_francisco"
KRK = "Krakow"
SYD = "Sydney"

employee_1 = Employee("Jackie", "1", Department(IT), Location(SF))
employee_2 = Employee("Molly", "2", Department(FINANCE), Location(SF))
employee_3 = Employee("Mark", "3", Department(IT), Location(KRK))
employee_4 = Employee("John", "4", Department(IT), Location(SYD))
employee_5 = Employee("Bob", "5", Department(FINANCE), Location(SYD))
employee_6 = Employee("Andrew", "6", Department(FINANCE), Location(KRK))
employee_7 = Employee("Tom", "7", Department(FINANCE), Location(SYD))
employee_8 = Employee("Gary", "8", Department(IT), Location(SF))
employee_9 = Employee("Martin", "9", Department(IT), Location(SF))

schedule_trainings(
    [
        employee_1,
        employee_2,
        employee_3,
        employee_4,
        employee_5,
        employee_6,
        employee_7,
        employee_8,
        employee_9,
    ]
)
```

To run example:

```
python example.py
```

Output:
```
Jackie is a new employee in San_francisco 🇺🇸
Jackie is joining IT department 💻
Molly is a new employee in San_francisco 🇺🇸
Molly is joining FINANCE department 💵
Mark is a new employee in Krakow 🇵🇱
Mark is joining IT department 💻
John is a new employee in Sydney 🇦🇺
John is joining IT department 💻
Bob is a new employee in Sydney 🇦🇺
Bob is joining FINANCE department 💵
Andrew is a new employee in Krakow 🇵🇱
Andrew is joining FINANCE department 💵
Tom is a new employee in Sydney 🇦🇺
Tom is joining FINANCE department 💵
Gary is a new employee in San_francisco 🇺🇸
Gary is joining IT department 💻
Martin is a new employee in San_francisco 🇺🇸
Martin is joining IT department 💻

----------------- Required trainings -----------------

Required trainings for Jackie: security_team, hr_intro, health_training,
Required trainings for Molly: law_team, hr_intro, health_training,
Required trainings for Mark: security_team, hr_intro, health_training,
Required trainings for John: security_team, hr_intro, health_training,
Required trainings for Bob: law_team, hr_intro, health_training,
Required trainings for Andrew: law_team, hr_intro, health_training,
Required trainings for Tom: law_team, hr_intro, health_training,
Required trainings for Gary: security_team, hr_intro, health_training,
Required trainings for Martin: security_team, hr_intro, health_training,

----------------- Scheduled trainings -----------------

Trainings for Jackie: security_team miami Tue 9-17, hr_intro las_vegas Fri 8-10, health_training chicago Fri 9-14,
Trainings for Molly: law_team boston Wed 7-12, hr_intro las_vegas Fri 8-10, health_training chicago Fri 9-14,
Trainings for Mark: security_team warsaw Mon 9-17, hr_intro rzeszow Mon 8-10, health_training warsaw Fri 8-13,
Trainings for John: security_team melbourne Wed 9-17, hr_intro melbourne Mon 9-11, health_training perth Mon 10-15,
Trainings for Bob: law_team perth Fri 11-16, hr_intro melbourne Mon 9-11, health_training perth Mon 10-15,
Trainings for Andrew: hr_intro rzeszow Mon 8-10, health_training warsaw Fri 8-13,
Trainings for Tom: law_team perth Fri 11-16, hr_intro melbourne Mon 9-11, health_training perth Mon 10-15,
Trainings for Gary: security_team miami Tue 9-17, hr_intro las_vegas Fri 8-10, health_training chicago Fri 9-14,
Trainings for Martin: security_team miami Tue 9-17, hr_intro las_vegas Fri 8-10, health_training chicago Fri 9-14,
```

To run small tests:
```
python -m pytest -v tests/small
```

To run large tests:
```
python -m pytest -v tests/large
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

Please notice that `large-tests` are failing, and you need to add some logic because of this. By default, job stops execution after failed step

GitHub documentation: https://docs.pytest.org/en/6.2.x/usage.html#creating-junitxml-format-files

## 5. Matrix strategy
In our workflow we are using action `actions/setup-python` to setup Python 3.9 for test jobs. We would like to check if our library is also
working without problems with Python versions 3.10 and 3.11. Please modify workflow to run tests also with these versions.
Hint: you don't need to create new jobs. Try parametrization with matrix strategy

GitHub documentation: https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs

Please remember that we need to have JUnit logs from every execution (3.9, 3.10, 3.11 Python versions) Some parametrization here might also be needed

Can you combine small and large tests in one job definition with parametrization? Or even further one job definition, but
small tests should be run with all Python versions, but large tests only with 3.9 and 3.10?

## 6. Semantic Release
Please familiarize with .releaserc file as it is crucial for release process. Use action https://github.com/splunk/semantic-release-action to incorporates release process in your pipeline.
Try to use conventional commits syntax to create few releases.

Conventional Commits: https://www.conventionalcommits.org/en/v1.0.0/

Try to use action `haya14busa/action-update-semver` to update shorter tags like v1 v1.1 https://github.com/haya14busa/action-update-semver

## 7. PyPI release
This task is optional. We will present how to make a PyPI release. If you have a PyPI account you can do it as well, but it is not required by next tasks. Can we upload package with the same name?

## 8. Reusable workflow
GitHub allows to create workflows which can be reused in many repositories. We prepared workflow which lists PRs and issues for repository - https://github.com/kkania-splunk/gh-monitor-workflow
Use this worfklow in your repository. Examine logs from GitHub runs

GitHub documentation: https://docs.github.com/en/actions/using-workflows/reusing-workflows

Make a fork of reusable workflow and modify action to fail if there are any open issues. In the next step try to make this behaviour configurable.
This can be done by adding input to the workflow, which determines if we should fail or proceed always

## 9. Creating your own action
