# This is function displays solitaire card game based on difficulty and player mode

def select_cards(cards):
    print("\nYou can play", cards, "solitaire!\n") # print the selected solitaire game

# Main function to start the game
def play_cards():
    # prompt user for valid for difficulty level and player mode
    difficulty = input("Pick a difficulty (easy/hard): ").strip().lower() # normalise all user inputs when comparing
    player = input("Choose players to start game (single-player or multi-player): ").strip().lower()

    # select based on difficulty and player mode
    if difficulty == "hard":
        if player == "multi-player":
            select_cards("CardzMania")
        elif player == "single-player":
            select_cards("FreeCell")
        else:
            print("\nInvalid player input\n")
    elif difficulty == "easy":
        if player == "multi-player":
            select_cards("Spider")
        elif player == "single-player":
            select_cards("Klondike")
        else:
            print("\nInvalid player input\n")
    else:
        # User entered an invalid difficult level
        print("\nInvalid difficulty input!\n")

# ensures that function call runs only when the script is executed directly
if __name__ == "__main__":
    play_cards()
