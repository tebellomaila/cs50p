emoji = "\U0001F914"    # 🤔

def chatbot():
    global emoji
    say("Is there anyone there?")
    
    emoji = "\U0001F60A" # 😊
    say("Oh, hi there!")

def say(phrase):
    print(phrase + " " + emoji)


if __name__ == "__main__":
    chatbot()



