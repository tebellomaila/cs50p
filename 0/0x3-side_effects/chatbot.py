def chatbot():
    global emoji
    say("Is there anyone there?")
    emoji = "\U0001F60A" # 😊
    say("Oh, hi!")

def say(phrase):
    print(phrase + " " + emoji)

emoji = "\U0001F914"    # 🤔

if __name__ == "__main__":
    chatbot()



