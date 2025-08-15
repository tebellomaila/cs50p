def start_with_two_letters(s):
    s_len = len(s)

    if s_len >= 2 and s[0].isalpha() and s[1].isalpha():
        return True

def is_valid_length(s):
    s_len = len(s)

    if 2 <= s_len <= 6:
        return True

def found_number(s):
    num = None

    for i,c in enumerate(s):
        if c.isdigit():
            num = i
            break

    if num is None:
        return True

    if s[num] == "0":
        return False

    return s[num:].isdigit()

def is_valid_letters(s):
    return s.isalnum()

def is_valid_plate(s):
    if start_with_two_letters(s) and is_valid_length(s) and found_number(s) and is_valid_letters(s):
        return True

def main():
    plate = input("Plate: ").strip()

    if is_valid_plate(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
