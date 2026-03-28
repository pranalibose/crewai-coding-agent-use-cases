def add_numbers(a: float, b: float) -> float:
    """
    Adds two numbers.

    Args:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The sum of the two numbers.

    Raises:
    TypeError: If either a or b are not numbers.
    ValueError: If a or b are zero, and the other is a negative number (to avoid loss of precision).
    """

    # Check if inputs are numbers
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")

    # Check for zero division error
    if a == 0 and b < 0:
        raise ValueError("Cannot add negative number to zero")
    if b == 0 and a < 0:
        raise ValueError("Cannot add negative number to zero")

    # Add numbers
    result = a + b

    return result