SECRET = 30
MAX_ATTEMPTS = 3

def check_guess(n):
    """ Validate user's guessed number to secret number """
    
    if n > SECRET:
        print("Too high")
    elif n < SECRET:
        print("Too low")
    else:
        print(f"You guessed number #{SECRET}\n")

    return n == SECRET 

def main():
    """ Prompt user for input with the current attempt number """
    
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            user_input = input(f"Enter a number to guess (Attempt {attempt}/{MAX_ATTEMPTS}): ")
            number = int(user_input) # integer conversion

            if check_guess(number):
                print("You won")
                return
            else:
                print("Incorrect! Try again.")
        except ValueError:
            print(f"Error: {user_input} must be a number") # if conversion fails, raise an error message
    
    print("GAME OVER")



if __name__ == "__main__":
    main()
