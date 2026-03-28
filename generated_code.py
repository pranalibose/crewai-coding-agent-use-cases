def type_odd_numbers(start: int = 1, end: int = 10) -> None:
    """
    Type odd numbers between the given range.

    Args:
    - start (int): The start of the range (inclusive). Defaults to 1.
    - end (int): The end of the range (inclusive). Defaults to 10.

    Raises:
    - TypeError: If start or end is not an integer.
    - ValueError: If start is greater than end.

    Returns:
    None
    """
    # Check if start and end are integers
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Both start and end must be integers.")

    # Check if start is less than or equal to end
    if start > end:
        raise ValueError("Start must be less than or equal to end.")

    # Type odd numbers between the range
    for num in range(start, end + 1):
        if num % 2 != 0:
            print(f"Typing odd number: {num}")


### MAIN PROGRAM ###

if __name__ == "__main__":
    try:
        # Call the function with default values
        type_odd_numbers()
        
        # Call the function with custom values
        print("\nTyping odd numbers between 5-15:")
        type_odd_numbers(5, 15)
        
    except TypeError as e:
        print(f"TypeError: {e}")
        
    except ValueError as e:
        print(f"ValueError: {e}")