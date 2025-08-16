def main():
    """ Prompt the user for their name and age and then greet the user"""
    print("Hello!")
    name = input("What's your name? ").strip() # Remove whitespaces

    if not name:
        print("Error: Please enter a valid name")
        return

    print(f"It is nice to meet, {name}")

    """ Validate age input and print message """
    try:
        age = int(input("What's your age? "))
        print(f"You will be {age + 1} years old after your birthday")
    except ValueError:
        print("Error: Please enter a numeric age")


if __name__ == "__main__":
    main()
