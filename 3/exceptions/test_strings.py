def main():
    try:
        # Get user input and convert to numbers
        a = input("Enter value of a: ")
        b = input("Enter value of b: ")
    
        # Validate division by zero
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")

        # Perform division and print the result
        print(f"Result: ", float(a / b))

    except ValueError:
        print("Error: Please enter valid numbers")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except BaseException as e:
        print(f"An unexpected error occurred : {type(e)}.name - {e}")


if __name__ == "__main__":
    main()
