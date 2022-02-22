import pytest
import src.calc_func as calc

NUMBER_1 = 3.0
NUMBER_2 = 2.0


def test_add():
    value = calc.add(NUMBER_1, NUMBER_2)
    assert value == 5.0, "Expected 5.0, got {}".format(value)


def test_subtract():
    value = calc.subtract(NUMBER_1, NUMBER_2)
    assert value == 1.0, "Expected 1.0, got {}".format(value)


def test_subtract_negative():
    value = calc.subtract(NUMBER_2, NUMBER_1)
    assert value == -1.0, "Expected -1.0, got {}".format(value)


def test_multiply():
    value = calc.multiply(NUMBER_1, NUMBER_2)
    assert value == 6.0, "Expected 6.0, got {}".format(value)


def test_divide():
    value = calc.divide(NUMBER_1, NUMBER_2)
    assert value == 1.5, "Expected 1.5, got {}".format(value)


# Test for dividing by zero catches the exception
# http://doc.pytest.org/en/latest/assert.html#assertions-about-expected-exceptions

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        calc.divide(NUMBER_1, 0)
    assert "division by zero" in str(e.value), "Expected 'division by zero'"


# Tests for maximum and minimum use parameters
# http://doc.pytest.org/en/latest/parametrize.html

@pytest.mark.parametrize("a, b, expected", [
    (NUMBER_1, NUMBER_2, NUMBER_1),
    (NUMBER_2, NUMBER_1, NUMBER_1),
    (NUMBER_1, NUMBER_1, NUMBER_1),
])
def test_maximum(a, b, expected):
    assert calc.maximum(a, b) == expected, "Expected {} for maximum".format(expected)


@pytest.mark.parametrize("a, b, expected", [
    (NUMBER_1, NUMBER_2, NUMBER_2),
    (NUMBER_2, NUMBER_1, NUMBER_2),
    (NUMBER_2, NUMBER_2, NUMBER_2),
])
def test_minimum(a, b, expected):
    assert calc.minimum(a, b) == expected, "Expected {} for minimum".format(expected)
