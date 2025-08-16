# defines a function that prompts the user to enter a guess number

def get_guess():
    # convert user input to integer and return a number
    number = int(input("Enter a guess number: "))
    return number

def main():
    number = get_guess()

    # check if `number` is 30. print "Correct!", otherwise "Incorrect!"
    if number == 30:
        print("Correct!")
    else:
        print("Incorrect!")

# call `main` to start the program
main()
