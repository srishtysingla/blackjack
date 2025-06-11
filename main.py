from game import Game


def main():
    print("Setting up Blackjack!")
    my_game = Game()
    my_game.setup()
    my_game.show_status()

    while my_game.has_ended == False:
        command = input("Do you want to Hit or Stand? ")
        if command == "Hit":
            my_game.player.hit(my_game.deck, my_game.dealer, my_game)
        elif command == "Stand":
            my_game.player.stand(my_game)
        else:
            print("Please enter a valid command")
        my_game.show_status()


if __name__ == "__main__":
    main()
