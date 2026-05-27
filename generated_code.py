import re

def validate_email(email: str) -> bool:
    """
    Validate whether a given text is a valid email or not.

    Args:
    - email (str): The text to be validated.

    Returns:
    - bool: True if the email is valid, False otherwise.
    """
    # Define the regex pattern for a valid email.
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    try:
        # Use the re.match function to check if the email matches the pattern.
        # re.match returns a match object if the string matches the pattern,
        # otherwise, it returns None.
        if re.match(pattern, email):
            return True
        else:
            return False
    except Exception as e:
        # Log any exception that occurs during validation.
        print(f"An error occurred during email validation: {str(e)}")
        return False


# Example usage:
if __name__ == "__main__":
    email = "example@example.com"
    if validate_email(email):
        print(f"'{email}' is a valid email.")
    else:
        print(f"'{email}' is not a valid email.")

    invalid_email = "example"
    if validate_email(invalid_email):
        print(f"'{invalid_email}' is a valid email.")
    else:
        print(f"'{invalid_email}' is not a valid email.")