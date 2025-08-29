months = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
]

def parse_date(date):
    """ Parse and validate a date input in numeric format (MM/DD/YYYY) or
    textual format (Month DD, YYYY) """

    if "/" in date:
        # Parse date input as a MM/DD/YYYY format
        date = [d.strip() for d in date.split("/")]
        
        if len(date) != 3:
            raise ValueError("Invalid date format")

        # Convert date values to integers
        month, day, year = map(int, date)

    elif " " in date:
        # Split date by spaces and check format (Month DD, YYYY)
        date = [d.strip() for d in date.split()]

        if len(date) != 2 or "," not in date[1].endswith(","):
            raise ValueError("Invalid date format")

        month, day, year = date

        # Remove comma from the day suffix
        day = day.rstrip(",")

        # Convert month to lowercase
        month = month.title()

        # Validate month is in the list (case-insensitive)
        if month not in months:
            raise KeyError("Invalid month name")

        month = months.index(month) + 1 # Convert month name to number
        print(month)
        day = int(day)
        year = int(year)

    else:
        raise ValueError("Invalid date format")

    # Validate month and day are numeric
    if not (month.isdigit() and day.isdigit()):
        raise ValueError("Day and month must be numeric")

    # Validate month and day ranges
    if not (1 <= month <= 12 or 1 <= day <= 31):
        raise ValueError("Day or Month is out of range")
    if year <= 0:
        raise ValueError("Year must be positive")
    
    return year, month, day


def main():
    """ Main function to handle user and output date in ISO 8601 format """

    while True:
        try:
            # Prompt the user for date
            date_str = input("Date: ").strip()

            # Parse and validate the date
            year, month, day = parse_date(date_str)

            # Format and output in YYYY-MM-DD format with zero padding
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break

        except (ValueError, IndexError, KeyError):
            continue    # If any conversion fails, prompt user again
        except (EOFError, KeyboardInterrupt):
            break   # handle control-d / control-c when detected to end the program gracefully


if __name__ == "__main__":
    main()
