class Player:
    def __init__(self):
        self.hand = []

    def hit(self, deck, dealer, game):
        dealer.deal(self, deck)
        if self.score() > 21:
            game.end()

    def score(self):
        result = 0
        for card in self.hand:
            result = result + card.value
        return result

    def show_hand(self):
        for card in self.hand:
            print(card.get_display_name())

    def stand(self, game):
        game.end()
