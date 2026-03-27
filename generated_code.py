# Function to swap two numbers in a tuple
def swap_two_numbers(numbers: tuple[int, int]) -> tuple[int, int]:
    """
    This function takes a tuple of two integers, swaps them and returns the new tuple.
    
    Args:
        numbers: A tuple of two integers.
    
    Returns:
        A new tuple with the numbers swapped.
    
    Raises:
        ValueError: If the input tuple does not have exactly two elements.
        TypeError: If the tuple elements are not integers.
    """
    if len(numbers) != 2:
        raise ValueError("Input tuple must have exactly two elements")
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("Tuple elements must be integers")
    return tuple(sorted(numbers))