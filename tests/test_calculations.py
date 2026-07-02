from geo_calculator import find_average

# from geo_calculator import _private_function
from geo_calculator.calculations import _private_function


def test_find_average_given_list_of_numbers():
    numbers = [1, 2, 3, 4, 5, 6]

    result = find_average(numbers)

    assert result == 3.5

def test_private_function_returns_private():
    result = _private_function()

    assert result == "private"
