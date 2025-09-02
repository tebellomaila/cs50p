def main():
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
    """
    return (starts_with_two_letters(s) and is_valid_length(s) and is_alphanum(s) and check_numbers(s))


def starts_with_two_letters(s):
    """
    Check if the plate starts with at least two letters.
    Return True if valid otherwise False.
    """
    return len(s) >= 2 and s[:2].isalpha()

def is_valid_length(s):
    """
    Check if the plate has between 2 and 6 characters.
    Return True if valid otherwise False.
    """
    return 2 <= len(s) <= 6

def is_alphanum(s):
    """
    Check if the plate contains only letters and numbers.
    Return True if valid otherwise False.
    """
    return s.isalnum()

def check_numbers(s):
    """
    Check that numbers are only at the end and the first number is not '0'.
    Return True if valid otherwise False.
    """

    # Find the first digit in the string
    for i, c in enumerate(s):
        if c.isdigit():
            # Check if the character is '0'
            if c == "0":
                return False
            # Check the rest of the characters are all numbers
            return s[i:].isdigit() # Letter after a number is invalid
    # If no digits found, it's valid (only letters)
    return True

if __name__ == "__main__":
    main()
