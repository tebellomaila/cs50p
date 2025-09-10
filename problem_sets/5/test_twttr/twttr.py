def shorten(s):
    """ Remove all vowels from the string input """

    # Use list comprehension to filter out vowels and then join the characters
    vowels = "aeiouAEIOU"
    return "".join([c for c in s if c not in vowels])

def main():
    # Prompt user for input and remove whitespaces
    string = input("Input: ").strip()

    # Process the string input to remove vowels and output the result
    result = shorten(string)

    print(f"Output: {result}")


if __name__ == "__main__":
    main()
