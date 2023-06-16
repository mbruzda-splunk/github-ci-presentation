import logging
import pytest

LOGGER = logging.getLogger("test-file")


class TestEmployee:
    def test_employee_init(self, employee):
        e = employee()
        assert e.name == "John"
        assert e._id == "1234"
        assert e.department.name == "IT"

    def test_get_name(self, employee):
        assert employee().get_name() == "John"

    @pytest.mark.parametrize(
        "name, nick",
        [("John", "Johnny"), ("Mark", "Mark"), ("Paul", "Paul")],
        ids=["case1", "case2", "case2"],
    )
    def test_get_nick(self, employee, name, nick):
        assert employee(name=name).get_nick() == nick

    @pytest.mark.parametrize(
        "employee_data, code",
        [(0, 50), (25, 50), (26, 100), (10000, 100)],
        indirect=True,
    )
    def test_get_employee_data(self, employee, employee_data, code):
        assert employee().get_employee_code(employee_data) == code
