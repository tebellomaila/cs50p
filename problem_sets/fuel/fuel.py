def main():
    """ Main function to calculate and display fuel percentage """
    
    while True:
        try:
            # Prompt user for fraction input
            fraction = input("Enter the fuel fraction (X/Y): ").strip()
        
            # Validate there is exactly one "/" character in the input
            if fraction.count("/") != 1:
                raise ValueError("Input must be in the format `X/Y`")


            # Split the fraction into X and Y values
            x, y = fraction.split("/")


            # Convert both values to integers
            x = int(x)
            y = int(y)
            
            # Validate that both values are positive integers and X <= Y
            if x < 0 or y < 0:
                raise ValueError("Both numbers must be positive integers")
            if x > y and y != 0:
                raise ValueError("Numerator cannot not be larger than denominator")

            # Calculate percentage and round to the nearest integer
            percentage = round((x / y) * 100)

            # Check for special cases
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")

            break # Exit loop after successful calculation
        
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
        except ZeroDivisionError:
            print(f"Error: Denominator cannot be zero. Please try again.")


if __name__ == "__main__":
    main()
