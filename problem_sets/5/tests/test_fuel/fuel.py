
def main():
    """ Main function to calculate and display the fuel percentage """
    while True:
        try:
            # Prompt the user for fraction input and convert to a percentage
            fraction = input("Enter the fuel level: ").strip()
            percentage = convert(fraction)

            # Validate and display the gauge reading
            reading = gauge(percentage)
            print(reading)
            break

        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}. Please try again")

def convert(fraction):
    """ Convert a fraction input to a percentage integer """
    if not isinstance(fraction, str):
        raise ValueError("Input must be a numeric string")
    if fraction.count("/") != 1:
        raise ValueError("Input must be in the format (X/Y)")
    # Split the fraction to x, y values 
    X, Y = fraction.split("/")

    # Convert both values to integers
    try:
        X, Y = int(X), int(Y)
    except ValueError:
        raise ValueError("Both numbers must be integers")

    # Validate that both values are positive and the numerator cannot be greater than the denominator
    if X < 0 or Y < 0:
        raise ValueError("Both numbers must be positive")
    if Y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if X > Y:
        raise ValueError("Numerator cannot be greater than denominator")

    # Calculate the percentage and round to the nearest integer
    percentage = round((X/Y) * 100)

    # Ensures the percentage ranges is between 0 and 100
    return max(0, min(100, round(percentage)))

def gauge(percentage):
    """ Convert a percentage to the appropriate gauge reading (E or F) """
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
