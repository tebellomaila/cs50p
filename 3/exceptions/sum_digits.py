def sum_digits(s):
    """ Returns sum of all digit characters in the string with debugging output """
    digits = 0

    for char in s:
        # Try to convert character to integer
        try:
            val = int(char)
            digits += val
        # Only catch ValueError (failed conversion)
        except ValueError:
            print(f"couldn't convert character '{char}'")
    return digits

def main():
    # Test cases
    test_strings = [
            "dajdka8923u8749",
            "23456789",
            "abcdefg"
    ]

    for s in test_strings:
        print(f"Sum of digits in '{s}': {sum_digits(s)}\n")


if __name__ == "__main__":
    main()
