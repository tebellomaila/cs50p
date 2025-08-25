def sum_digits(s):
    """ Returns sum of all digit characters in the string """
        
    #s is non-empty string containing digits
    return sum(int(char) for char in s if char.isdigit())

def main():
    # Test cases
    s1, s2, s3 = "dajdka8923u8749", "23456789", "abcdefg"
    print(f"Sum of digits in the string: {sum_digits(s1)}")
    print(f"Sum of digits in the string: {sum_digits(s2)}")
    print(f"Sum of digits in the string: {sum_digits(s3)}")



if __name__ == "__main__":
    main()
