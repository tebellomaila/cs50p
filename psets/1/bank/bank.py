def say(message):
    if message.startswith("hello"):
        return "$0"
    elif message.startswith("h") and not(message.startswith("hello")):
        return "$20"
    else:
        return "$100"

def main():
    greeting = input("Greeting: ").strip().lower()

    print(say(greeting))


main()


