def main():
    """ Main function to handle grocery list input and output """
    # Initialise empty grocery list (dictionary to store item counts)
    groceries = {}
    
    try:
        while True:
            # Prompt user for item (case-insensitive)
            item = input("Add item: ").strip().lower()

            # Update count for added item, handing possible KeyError
            try:
                groceries[item] += 1
            except KeyError:
                # Check if it item doesn't exist and then add it with count set to 1
                groceries[item] = 1

    except (EOFError, KeyboardInterrupt):
        # Handle control-d input when detected to exit the program gracefully
        print()

        if groceries:
            print("\nAdded items successfully")
            print("\nGrocery List")

            # Sort items alphabetically and output items in uppercase
            for item in sorted(groceries.keys()):
                print(f"{groceries[item]} {item.upper()}")
        else:
            print("No items found")


if __name__ == "__main__":
    main()
