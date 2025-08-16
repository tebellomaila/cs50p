# defines a function to displays solitaire card selector based on difficulty and player mode

#print selected cards game
def cards_selector(cards):
    print("You can play", cards, "solitaire")

# Main function to start the game selector
def main():
    # prompt user for valid difficulty level and player mode
    # normalise user inputs when comparing
    difficulty = input("Select a difficulty (easy/hard)? ").strip().lower()

    if not (difficulty == "easy" or difficulty == "hard"):
        print("Invalid difficulty entered")
        return

    player = input("Select a player to start game (single-player/multiplayer)? ").strip().lower()

    if not(player == "single-player" or player == "multiplayer"):
        print("Invalid number of players entered")
        return
    
    # select based on difficulty and player mode
    if difficulty == "easy" and player == "single-player":
        cards_selector("Klondike")
    elif difficulty == "easy" and player == "multiplayer":
        cards_selector("Spider")
    elif difficulty == "hard" and player == "single-player":
        cards_selector("FreeCell")
    else:
        cards_selector("CardzMania")

# ensures that function call runs only when the script is executed directly
if __name__ == "__main__":
    main()
