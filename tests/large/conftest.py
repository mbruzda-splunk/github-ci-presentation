import os
import itertools
import pytest

from jobsim import JOBSIM_PATH


@pytest.fixture
def failing():
    """
    Provide failing fixture for presentation purposes
    """
    raise ValueError("Wrong fixture")


def pytest_generate_tests(metafunc):
    """
    Parse the fixture dynamically.
    """
    for fixture in metafunc.fixturenames:
        if fixture.startswith("dynamic_location"):
            locations = []
            for _, _, filenames in os.walk(JOBSIM_PATH / "locations"):
                locations = [filename.split(".")[0] for filename in filenames]
            metafunc.parametrize(fixture, locations, ids=locations)
        elif fixture == "dynamic_employees":
            metafunc.parametrize(fixture, [2, 3, 4])
        elif fixture == "dynamic_departments":
            combinations = []
            for _, _, filenames in os.walk(JOBSIM_PATH / "departments"):
                departments = [filename.split(".")[0] for filename in filenames]
                combinations = list(itertools.combinations(departments, 2))
            metafunc.parametrize(
                fixture,
                combinations,
                ids=["-".join(departments) for departments in combinations],
            )


def pytest_configure(config):
    """
    Setup configuration after command-line options are parsed
    """
    config.addinivalue_line(
        "markers", "dynamic: tests which use fixtures with dynamically created values"
    )


def pytest_collection_modifyitems(session, config, items):
    for item in items:
        if all(departament in item.name for departament in ("finance", "hr")):
            item.add_marker("skip")
