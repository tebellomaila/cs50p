def meow():
    """ Prompt the user until a valid positive integer """
    while True:
        try:
            num = int(input("How many word sounds do you want to make? "))
            if num > 0:
                return num
            else:
                print("InputError: expected a positive number\n")
        except ValueError:
            print("InputError: expected a numeric input\n")

def main():
    # Get the number from user
    words_count = meow()

    # Iterate `n` times
    for word in range(words_count):
        print("meow!")


if __name__ == "__main__":
    main()
