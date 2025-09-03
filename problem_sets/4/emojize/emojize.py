import emoji

def main():
    """ Prompt the user for text and convert any emoji alias therein to their correspoding emoji """
    # Prompt user for input and convert emoji alias to actual emoji
    text = input("Input: ").strip()
    print(f"Output: {emoji.emojize(text)}")

if __name__ == "__main__":
    main()
