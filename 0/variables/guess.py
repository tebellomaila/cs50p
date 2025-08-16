SECRET = 30
MAX_ATTEMPTS = 3

def get_hint(guess):
    """ Return hint message based on guessed number """
    
    if guess > SECRET:
        return "too high"
    elif guess < SECRET:
        return "too low"
    
    return "You lost"
 

def main():
    """ Prompt user for input with the current attempt number """
    
    for attempt in range(1, MAX_ATTEMPTS + 1):
        while True:
            try:
                user_input = input(f"Enter a number to guess (Attempt {attempt}/{MAX_ATTEMPTS}): ")
                
                guess = int(user_input) # integer conversion 
                break   # exit inner loop on valid input

            except ValueError:
                print(f"Error: expected a number. `{user_input}` is an invalid input.") # if conversion fails, raise an error message

        if guess == SECRET:
            print(f"You guessed the secret number. You won!")
            return
       
        
        hint = get_hint(guess)
        prefix = f"The number you guessed was {hint}. Try again" if attempt < MAX_ATTEMPTS else ""
        print(prefix)
            
    
    print(f"The secret number was {SECRET}")



if __name__ == "__main__":
    main()
