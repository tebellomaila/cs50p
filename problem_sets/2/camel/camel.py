def snake_case(camel_str):
    """ Convert a CamelCase string to snake case """

    # If the input string is empty, return an empty string
    if not camel_str:
        return ""

    # Convert the first character to lowercase
    snake_chars = [camel_str[0].lower()]

    # Iterate over the remaining characters and then add underscore if a character is uppercase
    for char in camel_str[1:]:
        if char.isupper():
            snake_chars.append("_")
            snake_chars.append(char.lower())
        else:
            snake_chars.append(char)

    # Concatenate the characters into a string
    return "".join(snake_chars)

def main():
    camel_str = input("CamelCase: ")
    snake_str = snake_case(camel_str)
    print(f"snake_case: {snake_str}")


if __name__ == "__main__":
    main()
