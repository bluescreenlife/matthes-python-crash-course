from employee import Employee
import pytest

@pytest.fixture
def dummy_employee():
    dummy_employee = Employee("Andrew", "VanderLeest", 46500)
    return dummy_employee

    
def test_give_default_raise(dummy_employee):
    dummy_employee.give_raise()
    assert dummy_employee.annual_salary == 51500


def test_give_custom_raise(dummy_employee):
    dummy_employee.give_raise(20000)
    assert dummy_employee.annual_salary == 66500