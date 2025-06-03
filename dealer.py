class Dealer:
    def __init__(self):
        self.hand = []

    def deal(self, player, deck):
        card = deck.draw()
        player.hand.append(card)

    def score(self):
        result = 0
        for card in self.hand:
            result = result + card.value
        return result

    def show_hand(self):
        for card in self.hand:
            print(card.get_display_name())
