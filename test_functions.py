# test_functions.py
from functions import add, subtract, multiply
from functions import convert_fahrenheit_to_celsius as f2c
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'

# Uncomment this test in step 5
def test_subtract():
     assert subtract(2, 3) == -1

# Uncomment this test in step 11
# def test_convert_fahrenheit_to_celsius():
#     assert f2c(32) == 0
#     assert f2c(122) == pytest.approx(50)
#     with pytest.raises(AssertionError):
#         f2c(-600)

# def test_convert_fahrenheit_to_celsius():
#     assert f2c(32) == 0          # Freezing point
#     assert f2c(212) == 100       # Boiling point
#     assert f2c(98.6) == pytest.approx(37)  # Body temperature
#     with pytest.raises(AssertionError):
#         f2c(-600)  # This should fail


from functions import convert_fahrenheit_to_celsius as f2c

def test_convert_fahrenheit_to_celsius():
    assert f2c(32) == 0          # Freezing point
    assert f2c(212) == 100       # Boiling point
    assert f2c(98.6) == pytest.approx(37)  # Body temperature
    with pytest.raises(ValueError):  # Expect ValueError for impossible temperature
        f2c(-600)  # This should raise ValueError
