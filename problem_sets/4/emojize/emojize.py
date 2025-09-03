import emoji    # Import emoji loads the emoji library for converting text codes to actual emojis

def main():
    """ Prompt the user for text and convert any emoji alias therein to their correspoding emoji """
    # Prompt user for input and convert emoji alias to actual emoji
    text = input("Input: ").strip()
    print("Output:", emoji.emojize(text, language="alias"))

if __name__ == "__main__":
    main()
