
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
    if not fraction.count("/") == 1:
        raise ValueError("Expected the format X/Y")
    
    # Split the fraction to x, y values and convert to integer
    x, y = fraction.split("/")
    x, y = int(x), int(y)

    # Validate that both values are positive and the numerator is not greater than the denominator
    if x < 0 or y < 0:
        raise ValueError("Both numbers must be positive")
    if x > y:
        raise ValueError("Numerator cannot be greater than denominator")
    if y == 0:
        raise ZeroDivisionError("Denominator cannot zero")

    # Calculate the percentage and round to the nearest integer
    return round((x/y) * 100)

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
