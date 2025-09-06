import random   # Import random for generating random numbers
import sys

def get_positive_number():
    """ Prompt the user for a positive integer until a valid input is provided """
    while True:
        try:
            n = int(input("Level: "))

            # Validate that the number is positive
            if n < 0:
                continue
            return n
        except ValueError:
            continue
        except KeyboardInterrupt:
            sys.exit("\nGame stopped by user")

def main():
    """ Main function implements a number guessing game where the user specifies the range and the program generates a random number to guess """

    # Prompts the user for a level
    n = get_positive_number()

    # Generate a random number between 1 and n (inclusive)
    target = random.randint(1,n)

    # Main game loop for guessing
    while True:
        try:
            # Prompt the user to guess that number
            guess = int(input("Guess: "))

            # Validate the guess is a positive number
            if guess <= 0:
                continue

            # Check the guess against the target number
            if guess < target:
                print("Too small!")
            elif guess > target:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            continue
        except KeyboardInterrupt:
            sys.exit("\nGame stopped by user")


if __name__ == "__main__":
    main()
