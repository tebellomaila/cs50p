def get_guess():
    guess = int(input("Guess a number: "))
    return guess

def main():
    guess = get_guess()

    if guess == 30:
        print("Correct!")
    else:
        print("Incorrect!")

main()
