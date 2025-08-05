def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")

    return text

def main():
    message = input().strip()

    print(convert(message))
    
if __name__ == "__main__":
    main()
