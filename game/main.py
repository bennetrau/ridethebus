from game.game import RideTheBus


def main():
    print("Ride the Bus the game!... v1.0.0\n")

    while True:
        play_game()

        choice = input("Play again or exit? (1 = Play again, 2 = Exit): ")
        while choice not in ['1', '2']:
            choice = input("Invalid input. Enter 1 to play again or 2 to exit: ")
        if choice == '2':
            break

def play_game():

    print("starting game\n")
    game = RideTheBus()
        
    #R1
    guess = input("Round 1 - Guess color (red/black): ").lower()
    result, card = game.game(1, guess)
    print(f"Card was: {card['display']}\n")
    print(f"You guessed: {guess} \nResult: {result}\n")
    if result == guess:
        print("Correct!\n")
    else:
        print("Loser! Game over.\n")
        return

    # R2
    guess = input("Round 2 - Guess high or low (than previous card): ").lower()
    result, card = game.game(2, guess)
    print(f"Card was: {card['display']}\n")
    print(f"You guessed: {guess} \n Result: {result}\n\n")
    if result == guess:
        print("Correct!\n")
    else:
        print("Loser! Game over.\n")
        return

    # R 3
    guess = input("Round 3 - Guess aoutside or in between the last two card: ").lower()
    result, card = game.game(3, guess)
    print(f"Card was: {card['display']}\n")
    print(f"You guessed: {guess} \n Result: {result}\n\n")
    if result == guess:
        print("Correct!\n")
    else:
        print("Loser! Game over.\n")
        return

    # R4
    guess = input("Round 4 - Guess the suit (Hearts/Diamonds/Spades/Clubs): ").capitalize()
    result = game.game(4, guess)
    print(f"Card was: {game.player.cards[-1]['display']}\n")
    print(f"You guessed: {guess} \n Result: {result}\n\n")


if __name__ == "__main__":
    main()        