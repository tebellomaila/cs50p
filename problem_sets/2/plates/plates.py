def main():
        """
    Main function that handles user input and output.
    Prompts the user for a vanity plate, validates it, and prints the result.
    """
    # Prompt the user for plate number and convert to uppercase for case-insensitive validation
    plate = input("Plate: ").strip().upper()
    # Validate the number plate
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """
    Check if the plate meets all of the requirements.
    Return True if valid otherwise False

    Requirements:
    1. Must be between 2 and 6 characters
    2. Must start with at least two letters
    3. Must contain only alphanumeric characters
    4. Numbers must be at the end (no letters after numbers)
    5. The first number used cannot be zero
    """

    # Check if the plate has between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if the first two characters are letters
    if not s[:2].isalpha():
        return False
    
    # Check all characters are alphanumeric
    if not s.isalnum():
        return False

    # Check number placement and first characters is not zero
    is_number = False
    for c in s:
        if c.isdigit():
            if not is_number and c == '0':
                return False    # First number cannot be zero
            is_number = True
        elif is_number:
            return False    # Letter after number is invalid
    return True


if __name__ == "__main__":
    main()
