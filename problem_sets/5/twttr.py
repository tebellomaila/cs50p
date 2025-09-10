def shorten(s):
    """ Remove all vowels from input string """

    # Use list comprehension to filter out vowels and then join the characters
    vowels = "aeiouAEIOU"
    return "".join([c for c in s if c not in vowels])

def main():
    # Prompt user for input and remove whitespaces
    string = input("Input: ").strip()

    # Process the input to remove vowels in the input string and output the result
    result = shorten(string)

    print(f"Output: {result}")


if __name__ == "__main__":
    main()
