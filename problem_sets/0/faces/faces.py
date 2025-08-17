""" the convert function replaces ":)" with a smiling emoji and ":(" with a frowning emoji """

def convert(text):
    return text.replace(":)","😊").replace(":(","🙁")

def main():
    """ Prompt the user for input and outputs that same message with replaced emojis """
    message = input("Type your message here with some emoticons: ")
    print(convert(message))


if __name__ == "__main__":
    main()
