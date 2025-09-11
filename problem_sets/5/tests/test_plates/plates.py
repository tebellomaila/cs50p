def main():
    """Main function to prompt the user for a plate number and validates it meets all of the requirements. """

    # Prompt the user for plate number and convert to uppercase for case-insensitive validation
    plate = input("Plate: ").strip().upper()

    # Validate the plate number
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """ Check if the plate meets all of the requirements and returns True if valid otherwise False

    Requirements:
    1. Must be between 2 and 6 characters
    2. Must start with at least two letters
    3. Must contain only alphanumeric characters
    4. Numbers must be at the end (no letters after numbers)
    5. The first number used cannot be zero

    """

    # Check if the plate has between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Check if the first two characters are letters
    if not s[:2].isalpha():
        return False

    # Check if all characters are alphanumeric
    if not s.isalnum():
        return False

    # Check for the number placement and find the first number in the string input
    for i, c in enumerate(s):
        if c.isdigit():
            # Check the characters in the string from this index to the end must be digits
            if not s[i:].isdigit():
                return False
            # Check if the first number is not zero
            if c == "0":
                return False
            break
    return True


if __name__ == "__main__":
    main()
