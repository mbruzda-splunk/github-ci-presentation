import random
import pytest
import names

from jobsim.employee import Employee
from jobsim.location import Location
from jobsim.department import Department
from jobsim.trainings_scheduler import schedule_trainings


@pytest.mark.parametrize(
    "location, result",
    [
        (
            "Krakow",
            {
                "health_training": "warsaw Fri 8-13",
                "hr_intro": "rzeszow Mon 8-10",
                "security_team": "warsaw Mon 9-17",
            },
        ),
        (
            "San_Francisco",
            {
                "health_training": "boston Wed 7-12",
                "hr_intro": "boston Thur 7-9",
                "security_team": "miami Tue 9-17",
            },
        ),
        (
            "Sydney",
            {
                "health_training": "perth Mon 10-15",
                "hr_intro": "canberra Thur 7-9",
                "security_team": "melbourne Wed 9-17",
            },
        ),
    ],
)
def test_trainings_scheduled(location, result):
    location = Location(location)
    department = Department("it")
    e = Employee(names.get_first_name(), random.randint(1, 1000), department, location)
    schedule_trainings([e])
    assert e.scheduled_trainings == result
    assert len(e.scheduled_trainings) == len(e.department.info.trainings)


@pytest.mark.dynamic
def test_trainings_scheduled_dynamic_parametrization(
    dynamic_location, dynamic_employees
):
    dynamic_location = Location(dynamic_location)
    department = Department("it")
    employees = []
    for i in range(dynamic_employees):
        employees.append(
            Employee(
                names.get_first_name(),
                random.randint(1, 1000),
                department,
                dynamic_location,
            )
        )
    schedule_trainings(employees)
    for employee in employees:
        assert len(employee.scheduled_trainings) == len(
            employee.department.info.trainings
        ), f"Not all trainings for {employee.name} from {employee.department.name} in {employee.location.name} were scheduled."


@pytest.mark.dynamic
def test_trainings_scheduled_dynamic_parametrization_two_departments(
    dynamic_location, dynamic_departments, dynamic_employees
):
    dynamic_location = Location(dynamic_location)
    employees = []
    for department in dynamic_departments:
        for _ in range(dynamic_employees):
            employees.append(
                Employee(
                    names.get_first_name(),
                    random.randint(1, 1000),
                    Department(department),
                    dynamic_location,
                )
            )
    schedule_trainings(employees)
    for employee in employees:
        assert len(employee.scheduled_trainings) == len(
            employee.department.info.trainings
        ), f"Not all trainings for {employee.name} from {employee.department.name} in {employee.location.name} were scheduled."


def test_fail_fixture(failing):
    assert 1 == 1


@pytest.mark.parametrize("chance_to_pass", [10, 30, 50, 75, 90])
def test_flaky_scenario(chance_to_pass):
    assert (
        100 * random.random() < chance_to_pass
    ), f"Test is passing with {chance_to_pass}% propability"
