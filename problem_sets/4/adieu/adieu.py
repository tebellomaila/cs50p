import inflect  # Import inflect module for natural language formatting and joining names
import sys

def main():
    """ Main function reads names from the user input and bids adieu with proper grammatical formatting using Oxford commas """

    names = []
    p = inflect.engine()    # Initiliase the inflect engine for nlp
    
    try:
        # Iterate through the loop until EOF is detected
        while True:
            try:
                # Read input from the user
                name = input("Name: ").strip()
                
                # Empty line ends input and add non-empty name to the list
                if not name:
                    continue
                names.append(name.title())

            except EOFError:
                break       # Exit loop when control-d is pressed
    except KeyboardInterrupt:
        pass

    # Checks if names were entered in the list and use inflect to format the names grammatically
    if names:
        print(f"\nAdieu, adieu, to {p.join(names)}")
    else:
        # Exit properly if no names were provided
        sys.exit("\nNo names were entered")


if __name__ == "__main__":
    main()
