# FDA fruit calorie data per serving based on FDA poster
fruit_calories = {
    "apple": 130, "avocado": 50,"banana": 110,
    "cantaloupe": 50, "grapefruit": 60, "grapes": 90,
    "honeydew melon": 50, "kiwifruit": 90, "lemon": 15,
    "lime": 20, "nectarine": 60, "orange": 80,
    "peach": 60, "pear": 100, "pineapple": 50,
    "plums": 70, "strawberries": 50, "sweet cherries": 100,
    "tangerine": 50, "watermelon": 80
    }

def main():
    """ Check if fruit exists in calorie data and return its calories """
    try:
        # Prompt user for fruit name and normalise to lowercase
        fruit_name = input("Item: ").strip().lower()

        # Try to retrieve and print the calorie count
        calories = fruit_calories[fruit_name]
        print(f"Calories: {calories}")
    except KeyError:
        # Handle case where the input is not a recognised fruit
        pass
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
