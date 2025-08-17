def main():
    """ Prompt the user for input and outputs the same input with spaces replaced with "..." periods """
    text = input("Type your text here: ").replace(" ", "...")
    print(text)


if __name__ == "__main__":
    main()
