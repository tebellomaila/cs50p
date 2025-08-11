# Function prompts the user to a guess number

def get_guess():
    # it converts the input to an integer and returns it
    number = int(input("Enter a guess number: "))
    return number

def main():
    number = get_guess()

    # it check if the number is 30. if so, it prints "Correct!", otherwise "Incorrect!"
    if number == 30:
        print("Correct!")
    else:
        print("Incorrect!")

# call `main' to start the program
main()
