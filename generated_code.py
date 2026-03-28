"""
Module for generating a list of numbers from 1 to 10.
"""

import logging

def generate_numbers(n: int = 10) -> list[int]:
    """
    Generates a list of numbers from 1 to n.

    Args:
    n (int): The upper limit of the list (default is 10).

    Returns:
    list[int]: A list of numbers from 1 to n.

    Raises:
    ValueError: If n is not a positive integer.
    """
    try:
        assert isinstance(n, int) and n > 0, "n must be a positive integer"
        return list(range(1, n + 1))
    except AssertionError as e:
        logging.error(f"Invalid input: {e}")
        raise

# Example usage:
numbers = generate_numbers(10)
print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]