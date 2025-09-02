def main():
    try:
        # Get user input and convert to numbers
        a = float(input("Enter value of a: "))
        b = float(input("Enter value of b: "))
    
        # Validate division by zero
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")

        # Perform division and print the result
        print(f"Result: {a / b}")

    except ValueError:
        print("Error: Please enter valid numbers")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred : {type(e)}.name - {e}")


if __name__ == "__main__":
    main()
