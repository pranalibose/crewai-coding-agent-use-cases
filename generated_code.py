def add_two_numbers(num1: float, num2: float) -> float:
    """
    Add two numbers.

    Args:
    - num1 (float): The first number.
    - num2 (float): The second number.

    Returns:
    - float: The sum of num1 and num2.

    Raises:
    - TypeError: If either num1 or num2 is not a number.
    - ValueError: If either num1 or num2 is NaN (Not a Number).
    """
    try:
        # Attempt to validate and add the numbers
        if not isinstance(num1, (int, float)):
            raise TypeError("num1 should be a number.")
        if not isinstance(num2, (int, float)):
            raise TypeError("num2 should be a number.")

        if isinstance(num1, float) and num1 != num1:  # Check for NaN
            raise ValueError("num1 cannot be NaN.")
        if isinstance(num2, float) and num2 != num2:  # Check for NaN
            raise ValueError("num2 cannot be NaN.")

        # Return the sum of num1 and num2
        return num1 + num2

    except TypeError as te:
        # Handle type-related errors
        raise te

    except ValueError as ve:
        # Handle NaN-related errors
        raise ve

    except Exception as e:
        # Handle unexpected errors
        raise Exception("An unexpected error occurred.") from e


# Example usage:
if __name__ == "__main__":
    try:
        # Example 1: Valid numbers
        result1 = add_two_numbers(5, 10)
        print(f"5 + 10 = {result1}")

        # Example 2: Invalid type (number)
        result2 = add_two_numbers("five", 10)
        print(f"'five' + 10 = {result2}")  # Should raise an error

    except Exception as e:
        # Catch and print any error that occurs during execution
        print(f"Error: {str(e)}")