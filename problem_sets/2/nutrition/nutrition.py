def main():
    """ Check if fruit exists in calorie data and return its calories """

    # FDA fruit calorie as per serving based on FDA poster
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }
    
    # Prompt user for fruit input (case-insensitive)
    fruit = input("Item: ").strip().lower()
    

    if fruit in fruit_calories:
        # Output calories if fruit is found
        print(f"Calories: {fruit_calories[fruit]}")


if __name__ == "__main__":
    main()
