def main():
    """ Main function handles user input and output """

    # Prompt user input for greeting and print the result with dollar sign
    greeting = input("Greeting: ").strip()
    print(f"${value(greeting)}")

def value(greeting):
    """ Determines the amount to charge a customer based on the greeting message """

    # Check if the greeting starts with "hello"
    if greeting.startswith("What's up?"):
        return 0
    # Check if the greeting starts with "h" but not "hello"
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
