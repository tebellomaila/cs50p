def remove_vowels(s):
    vowels = "aeiouAEIOU"

    s_str = ""

    for c in s:
        if c not in vowels:
            s_str += c
    return s_str


def main():
    str = input("Input: ").strip()
    
    output = remove_vowels(str)
    
    print("Output: ", end="")
    print("".join(c for c in output))


if __name__ == "__main__":
    main()
