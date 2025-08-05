def get_number():
    # prompt the user until a valid positive integer
    while True:
        number = int(input("How many word sounds do you want to make? "))
        # checks if the number is positive
        if number > 0:
            return number # return valid input
        else:
            print("Input error: expected a positive number\n")

def meow(n):
    # print "meow!" `n` times
    for _ in range(n):
        print("meow!")


if __name__ == "__main__":
    # get user input
    number = get_number()

    meow(number)
