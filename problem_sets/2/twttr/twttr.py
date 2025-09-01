def remove_vowels(string):
    """ Remove all vowels from input string """

    # Use list comprehension to filter out vowels and then join the characters
    vowels = "aeiouAEIOU"
    return "".join([char for char in string if char not in vowels])

def main():
    # Prompt user for input and remove whitespaces
    input_str = input("Input: ").strip()

    # Process the input to remove vowels in the input string
    output_str = remove_vowels(input_str)

    print(f"Output: {output_str}")


if __name__ == "__main__":
    main()
