import random       # For generating random numbers for math problems
import sys          # For system exit functionality

def main():
     """ Main fuction for generating the math problems and prompting the user to addition problems """

     # Initialize the score counter
     score = 0
     #Get the difficulty level from the user input
     level = get_level()

     # Generate random numbers for x, y values and output 10 math problems
     for _ in range(10):
         x = generate_integer(level)
         y = generate_integer(level)
         # Calculate the correct answer for the math problem
         answer = x + y

        # Allow the user up to 3 tries for each math problem
        for attempt in range(3):
            try:
                # Display the current problem and get user's answer
                user_answer = int(input(f"{x} + {y} = "))

                # Check if the user answer is correct
                if user_answer == answer:
                    score += 1
                    break           # Skip to the next math problem
                else:
                    print("EEE")    # Show `EEE` for incorrect answer
            except ValueError:
                # Handels non-integer inputs
                print("EEE")
            except KeyboardInterrupt:
                # Handles control-c during problem solving
                sys.exit(0)

            # If the third attempt is incorrect, output the correct answer
            if attempt == 2:
                print(f"{x} + {y} = {answer}")
    
    # Display the user's score
    print(f"Score: {score}")


def get_level():
    """ Prompt the user for a level until a valid is entered """
    while True:
        try:
            # Prompt the user for difficulty level
            level = int(input("Level: "))

            # Validate that level is 1, 2, or 3 otherwise reprompt the user for a valid level
            if level in [1,2,3]:
                return level
            else:
                pass
        except ValueError:
            # Reprompt the user for non-integer inputs
            continue
        except KeyboardInterrupt:
            sys.exit(0)         # Exit the program with status code 0

def generate_integer(level):
    """ Generates a randomly generated non-integer values for x and y with `n` number of digits """
    
    # Validate the difficulty level input
    if level not in [1,2,3]:
        raise ValueError("Level: ")
    # Generate random numbers base on the level entered
    match level:
        case 1: return random.randrange(0,10)
        case 2: return random.randrange(10,100)
        case 3: return random.randrange(100, 1000)
        _: pass


if __name__ == "__main__":
    main()
