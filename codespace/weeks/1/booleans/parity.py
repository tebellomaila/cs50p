# defines a function to determine the number is even
def is_even(n):
    return n % 2 == 0

# main function of the program
def main():
    # prompt user for a number
    num = int(input("Enter a number: "))

    # check if entered number is even
    if is_even(num):
        print("Even")
    else:
        print("Odd")


main()
