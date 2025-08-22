def snake_case(s):
    """ Convert a CamelCase string to snake case """
    
    snake_case = []

    # If the input string is empty, return an empty string
    if not s:
        return ""

    # Handle the first character
    if s[0].isupper():
        snake_case.append(s[0].lower())
    else:
        snake_case.append(s[0])

    # Iterate through the remaining characters
    for c in s[1:]:
        # If the character is uppercase, add an underscore first then convert to lowercase
        if c.isupper():
            snake_case.append("_" + c.lower())
        else:
            snake_case.append(c)

    # Join characters into a single string
    return "".join(snake_case)


def main():
    # Prompt user for CamelCase input
    camel_str = input("camelCase: ")

    # Convert the string to snake_case
    snake_str = snake_case(camel_str)

    print(f"snake_case: {snake_str}")    


if __name__ == "__main__":
    main()
