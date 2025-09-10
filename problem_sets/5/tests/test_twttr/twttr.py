def shorten(s):
    """ Remove all vowels from the string input """

    # Use a list comprehension to filter out vowels and then join the characters
    return "".join([c for c in s if c not in "aeiouAEIOU"])

def main():
    # Prompt user for input and remove whitespaces
    string = input("Input: ").strip()

    # Process the string input to remove vowels and output the result
    print(f"Output: {shorten(string)}")


if __name__ == "__main__":
    main()
