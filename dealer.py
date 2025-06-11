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
        for card in self.hand:
            if result <= 11 and card.rank == "Ace":
                result = result + 10
        return result

    def show_hand(self):
        for card in self.hand:
            print(card.get_display_name())
