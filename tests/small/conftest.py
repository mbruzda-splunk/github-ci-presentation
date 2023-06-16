from collections import namedtuple
import logging
import pytest

LOGGER = logging.getLogger("conftest")


@pytest.fixture(scope="session")
def employee(request):
    """
    Provide Employee instance for tests
    """

    def teardown():
        LOGGER.info("Fixture teardown")

    request.addfinalizer(teardown)
    LOGGER.info("Fixture setup")
    from jobsim.employee import Employee

    def func(name="John"):
        Location = namedtuple("Location", ["name", "info"])
        Info = namedtuple("Info", ["flag"])
        Department = namedtuple("Department", ["name", "info"])
        DepartmentInfo = namedtuple("DepartmentInfo", ["logo"])
        return Employee(
            name,
            "1234",
            Department("IT", DepartmentInfo("💻")),
            Location("Krakow", Info("🇵🇱")),
        )

    yield func


@pytest.fixture(params=["error", "000", 111, [1, 2, 3]])
def base_employee_data(request):
    """
    Provide base employee data
    """

    def func(departament_id):
        return {"departament_id": departament_id, "problematic_field": request.param}

    return func


@pytest.fixture
def employee_data(base_employee_data, request):
    """
    Provide employee data
    """
    return base_employee_data(request.param)


@pytest.fixture
def code(request):
    """
    Provide employee code
    """
    return request.param
