def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")

    return text

def main():
    message = convert(input())

    print(message)


main()
