def square_list(L):
    """ Squares each element in the list and returns new list with squared values """
    
    squared_L = [e ** 2 for e in L] 
    return squared_L 

def square_even(L):
    """ Checks if each element is even in the list and returns a new list even squared values """
    squared_L = [e ** 2 for e in L if e % 2 == 0]
    return squared_L

def main():
    # Test case
    n = int(input("Enter a range number: "))

    # Create a list of numbers from 1 to n
    numbers = list(range(1, n + 1))

    # Get squared values
    squared_n = square_list(numbers)
    squared_even = square_even(numbers)

    # Print the result without brackets
    print("Squared numbers: ", ", ".join(map(str, squared_n)))
    print("Squared even numbers: ", ", ".join(map(str, squared_even)))


if __name__ == "__main__":
    main()
