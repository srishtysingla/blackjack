from player import Player
from dealer import Dealer
from deck import Deck


class Game:
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()
        self.has_ended = False

    def setup(self):
        self.deck.shuffle()
        self.dealer.deal(self.player, self.deck)
        self.dealer.deal(self.player, self.deck)
        self.dealer.deal(self.dealer, self.deck)

    def end(self):
        self.dealer.deal(self.dealer, self.deck)
        if self.dealer.score() <= 16:
            self.dealer.deal(self.dealer, self.deck)
        winner = self.decide_winner()
        if winner == self.player:
            print("You won!")
        elif winner is None:
            print("It is a draw")
        else:
            print("You lost!")
        self.has_ended = True

    def decide_winner(self):
        player_score = self.player.score()
        dealer_score = self.dealer.score()
        if player_score > 21:
            return self.dealer
        elif dealer_score > 21:
            return self.player
        elif player_score > dealer_score:
            return self.player
        elif player_score == dealer_score:
            return None
        else:
            return self.dealer

    def show_status(self):
        print('Player:')
        self.player.show_hand()
        print(f'Score: {self.player.score()}')
        print('----')
        print('Dealer:')
        self.dealer.show_hand()
        print(f'Score: {self.dealer.score()}')
        print('----')
