from game import Game


def main():
    print("Setting up Blackjack!")
    my_game = Game()
    my_game.setup()
    my_game.show_status()

    while my_game.has_ended == False:
        command = input("Do you want to Hit or Stand? ")
        command = command.lower()
        if command == "hit":
            my_game.player.hit(my_game.deck, my_game.dealer, my_game)
        elif command == "stand":
            my_game.player.stand(my_game)
        else:
            print("Please enter a valid command")
        my_game.show_status()
    if my_game.winner == my_game.player:
        print("You won!")
    elif my_game.winner is None:
        print("It is a push")
    else:
        print("You lost!")


if __name__ == "__main__":
    main()
