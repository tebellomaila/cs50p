def sum_digits(s):
    """ Returns sum of all digit characters in the string """

    sum_digits = 0
    for char in s:
        try:
            val = int(char)
            sum_digits += val
        except:
            print(f"couldn't convert characeter '{char}'")
    return sum_digits

def main():
    # Test cases
    s1, s2, s3 = "dajdka8923u8749", "23456789", "abcdefg"
    print(sum_digits(s1))
    print(sum_digits(s2))
    print(sum_digits(s3))



if __name__ == "__main__":
    main()
