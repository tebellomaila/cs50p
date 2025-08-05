def select_cards(cards):
    print("\nYou can play", cards, "solitaire!\n")

def play_cards():
    difficulty = input("Pick a difficulty (easy/hard): ").strip().lower()

    if  not (difficulty == "easy" or difficulty == "hard"):
        print("\nPick a valid difficulty input!\n")
        return

    player = input("Choose players to start game (single-player or multi-player)): ").strip().lower()

    if not (player == "single-player" or player == "multi-player"):
        print("\nChoose a valid player input!\n")
        return

    if difficulty == "easy" and player == "single-player":
        select_cards("Klondike")
    elif difficulty == "hard" and player == "single-player":
        select_cards("FreeCell")
    elif difficulty == "easy" and player == "multi-player":
        select_cards("Spider")
    else:
        select_cards("CardzMania")

if __name__ == "__main__":
    play_cards()


