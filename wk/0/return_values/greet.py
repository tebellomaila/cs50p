def greet(message):
    if "hello" in message:
        return "hello, there"
    else:
        return "I'm not sure what you mean"

response = greet("how are you?")
print(response)
