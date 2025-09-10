def say(message):
    """ Determines the amount to charge a customer based on the greeting message """

    # Check if the greeting starts with "hello"
    if message.startswith("hello"):
        return "$0"
    # Check if the greeting starts with "h" but not "hello"
    elif message.startswith("h") and not(message.startswith("hello")):
        return "$20"
    else:
        return "$100"

def main():
    """ Main function handles user input and output """
    # Prompt for user input and convert to lowercase
    greeting = input("Greeting: ").strip().lower()
    print(say(greeting))


if __name__ == "__main__":
    main()

