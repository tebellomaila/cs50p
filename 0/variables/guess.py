# Define game constants
SECRET = 30         # The secret number to be guessed
MAX_ATTEMPTS = 3    # Maximum numbr of attempts allowed

def get_hint(guess):
    """ Return hint message based on guessed number """

    # Compare the guess with the secret number
    if guess > SECRET:
        return "too high"
    elif guess < SECRET:
        return "too low"
    
    return "correct" # Fixed: should return "correct"
 

def main():
    """ Prompt the user for input with the current attempt number """
    
    # Loop through each attempt from 1 to MAX_ATTEMPTS
    for attempt in range(1, MAX_ATTEMPTS + 1):
        while True:
            try:
                # Prompt the user for input until a valid input is provided
                number = input(f"Enter a number to guess (Attempt {attempt}/{MAX_ATTEMPTS}): ")
                
                # Convert input to integer
                guess = int(number) 
                break

            except ValueError:
                print(f"Error: Expected a number. `{number}` is an invalid input.") # if conversion fails, raise an error message

        # Check if the guess matches the secret number
        if guess == SECRET:
            print(f"You guessed the secret number. You won!")
            return
       
       # Get hint message based on the guess
        hint = get_hint(guess)
        prefix = f"The number you guessed was {hint}. Try again" if attempt < MAX_ATTEMPTS else "The number you guessed was {hint}"
        print(prefix)
            
    # Display the feedback to the user
    print(f"The secret number was {SECRET}")

# Tus ensures that the function call runs only when the script is executed directly
if __name__ == "__main__":
    main()
