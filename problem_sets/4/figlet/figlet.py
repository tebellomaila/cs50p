from pyfiglet import Figlet
from random import choice
import sys

def main():
        # Initialize the Figlet object
        figlet = Figlet()
        
        # Get list of available fonts from Figlet
        fonts = figlet.getFonts()

        # Validate command-line arguments before user input to avoid invalid prompts
        # Expected: 0 args (random font) or 3 args (script_name, flag, font_name)
        if len(sys.argv) not in [1, 3]:
            sys.exit("Invalid usage")

        # Handle case when user provides valid font
        if len(sys.argv) == 3:
            # Check if 1 arg is a valid font flag
            if sys.argv[1] not in ["-f", "--font"]:
                sys.exit("Invalid usage")

        try:
            # Prompt the user for text input
            text = input("Input: ").strip()
            # Check if the text input is empty
            if not text:
                sys.exit("Error: No text entered")

            # Handle font selection based on command-line arguments
            if len(sys.argv) == 1:
                f = choice(fonts)   # Random font selection
            else:
                # Store the specified name
                f = sys.argv[2]     # Use specified font
                # Check if the font exists in available fonts from figlet
                if f not in fonts:
                    sys.exit("Invalid usage")

            # Set the selected font in the Figlet object
            figlet.setFont(font=f)

            # Render and display the text in the selected font
            print(f"Output:\n {figlet.renderText(text)}")
        
        except KeyboardInterrupt:
            sys.exit("\nOperation cancelled by user")
        except Exception as e:
            sys.exit(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
