def snake_case(s):
    """ Convert a CamelCase string to snake case """
    
    snake_chars = []

    # If the input string is empty, return empty string
    if not s:
        return ""

    # Convert first character to lowercase
    snake_chars = [s[0].lower()]

    # Iterate through the remaining characters
    for c in s[1:]:
        # If the character is uppercase, add an underscore first then convert to lowercase
        if c.isupper():
            snake_chars.append("_")
            snake_chars.append(c.lower())
        else:
            snake_chars.append(c)

    # Join characters into a single string
    return "".join(snake_chars)


def main():
    """ Main function to handle user input and output conversion """
    camel_str = input("camelCase: ")
    snake_str = snake_case(camel_str)
    print(f"snake_case: {snake_str}")    


if __name__ == "__main__":
    main()
