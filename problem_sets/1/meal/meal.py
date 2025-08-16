def main():
    time_str = input("What time is it? ").strip()
    
    if len(time_str) != 0:
        hours = convert(time_str)

        if 7.0 <= hours <= 8.0:
            print("breakfast time")
        elif 12.0 <= hours <= 13.0:
            print("lunch time")
        elif 18.0 <= hours <= 19.0:
            print("dinner time")
        else:
            print(end = "")


def convert(time):
    hours, minutes = time.split(":")
    
    hours_float = float(hours)
    minutes_float = float(minutes) / 60

    return hours_float + minutes_float

if __name__ == "__main__":
    main()
