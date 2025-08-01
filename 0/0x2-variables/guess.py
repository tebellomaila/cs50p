def guess():
    number = int(input("Guess a number: "))
    return number

def main():
    number = guess()

    if number == 30:
        print("Correct!")
    else:
        print("Incorrect!")

main()
