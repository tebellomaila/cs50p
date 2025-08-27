def main():
    """ Main function to handle order input and print running total cost """

    # Menu dictionary with food items and prices
    menu = {
            "Baja Taco": 4.00,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
    }

    total = 0.0

    try:
        while True:
            # Prompt user for food item input
            item = input("Enter food item in the menu: ").strip().title()
            
            # Check the item exists in the menu and then calculate the total cost
            if item in menu:
                total += menu[item]
                print(f"Total: ${total:.2f}")
            else:
                print("Item not found in the menu. Please try again")

    except EOFError:
        # Handle control-d input detected
        print("\nOrder is completed successfully. Thank you!")
    except KeyboardInterrupt:
        # Handle control-c input detected
        print("\nOrder is cancelled successfully")


if __name__ == "__main__":
    main()
