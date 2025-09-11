def main():
    """ Main function that handles user input and output """
    
    # Prompts the user for a vanity plate, validates it, and prints the result
    plate = input("Plate: ").strip().upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """
    Check if the plate meets all of the requirements.
    Return True if valid otherwise False
    """

    # Check if the plate has between 2 and 6 characters
    if  len(s) <= 2 or len(s) >= 6:
        # Check if the first two characters are letters
        if s.isalpha():
            return True
        # Check all characters are alphanumeric
        elif s.isalnum() and s[:2].isalpha():
            # Check number placement and first characters is not zero
            for c in s:
                if c.isdigit():
                    # First number cannot be zero
                    pos = s.index(c)
                    if s[pos:].isdigit() and int(c) != 0:
                        return True
                    else:
                        return False    # Letter after number is invalid
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
