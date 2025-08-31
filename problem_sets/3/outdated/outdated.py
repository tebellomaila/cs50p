months = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
]

def parse_date(date):
    """ Parse and validate a date input in numeric format (MM/DD/YYYY) or
    textual format (Month DD, YYYY) """
    
    # Handle the date numeric format (MM/DD/YYYY)
    if "/" in date:
        # Split and strip the date input into month, day and year
        date_list = [d.strip() for d in date.split("/")]
        
        # Validate the date token count matches the numeric format 
        if len(date_list) != 3:
            raise ValueError("Invalid input. Expected MM/DD/YYYY")

        try:
            # Convert the date values to integers
            month, day, year = map(int, date_list)
        except ValueError:
            raise ValueError("Month, day and year must be numbers")

        # Validate the month and day ranges
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        if not (1 <= day <= 31):
            raise ValueError("Day must be between 1 and 31")
        if year <= 0:
            raise ValueError("Year must be positive")
        
        return year, month, day
    
    # Handle the date textual format (Month DD, YYYY)
    elif "," in date:
        # Split into date portion and year portion
        date_list = [d.strip() for d in date.split(",")]
        if len(date_list) != 2:
            raise ValueError("Invalid input. Expected to be 'Month DD, YYYY'")

        year_str = date_list[1]

        # Extract the month and day
        month_day = date_list[0]

        # Split date portion into month name and day
        try:
            month_str, day_str = month_day.split()
        except ValueError:
            raise ValueError("Invalid input. Expected to be 'Month DD, YYYY'")

        # Convert month to title case and find its index
        month_str = month_str.title()
        if month_str not in months:
            raise ValueError("Invalid month name. Expected to be 'Month DD, YYYY'")
        month = months.index(month_str) + 1

        try:
            day = int(day_str)
            year = int(year_str)
        except ValueError:
            raise ValueError("Day and year must be numbers")

        # Validate day and year ranges
        if not (1 <= day <= 31):
            raise ValueError("Day must be between 1 and 31")
        if year <= 0:
            raise ValueError("Year must be positive")

        return year, month, day

    else:
        raise ValueError("Unrecognised date format")


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

        except ValueError as e:
            # If any conversion fails, prompt user again
            print(f"Error: {e}")
            continue
        except (EOFError, KeyboardInterrupt):
            # handle Ctrl+D / Ctrl+C when detected to end the program
            break


if __name__ == "__main__":
    main()
