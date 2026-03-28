# add_two_numbers.py
"""
Module for adding two numbers.

Provides a function to add two numbers, handling errors and providing type hints.
"""

from typing import Union

def add_two_numbers(num1: Union[int, float], num2: Union[int, float]) -> float:
    """
    Adds two numbers together.

    Args:
        num1 (int | float): The first number to add.
        num2 (int | float): The second number to add.

    Returns:
        float: The sum of the two numbers.

    Raises:
        TypeError: If either num1 or num2 is not a number.
        ValueError: If num1 or num2 is NaN (not a number).
    """
    # Check if inputs are numbers
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Both inputs must be numbers")

    # Check if inputs are not NaN
    if num1 != num1 or num2 != num2:
        raise ValueError("Input values cannot be NaN (not a number)")

    # Add the numbers together
    result = num1 + num2

    return result

# Test cases
print(add_two_numbers(5, 10))  # Output: 15.0
print(add_two_numbers(3.5, 2.5))  # Output: 6.0

# Error handling
try:
    print(add_two_numbers(5, "10"))  # Raises TypeError
except TypeError as e:
    print(e)  # Output: Both inputs must be numbers

try:
    print(add_two_numbers(5, float('nan')))  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Input values cannot be NaN (not a number)