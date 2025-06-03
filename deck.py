import random


class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    def get_display_name(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.cards = [
            Card('Ace', 'Spade', 1),
            Card('2', 'Spade', 2),
            Card('3', 'Spade', 3),
            Card('4', 'Spade', 4),
            Card('5', 'Spade', 5),
            Card('6', 'Spade', 6),
            Card('7', 'Spade', 7),
            Card('8', 'Spade', 8),
            Card('9', 'Spade', 9),
            Card('10', 'Spade', 10),
            Card('Jack', 'Spade', 10),
            Card('Queen', 'Spade', 10),
            Card('King', 'Spade', 10),

            Card('Ace', 'Heart', 1),
            Card('2', 'Heart', 2),
            Card('3', 'Heart', 3),
            Card('4', 'Heart', 4),
            Card('5', 'Heart', 5),
            Card('6', 'Heart', 6),
            Card('7', 'Heart', 7),
            Card('8', 'Heart', 8),
            Card('9', 'Heart', 9),
            Card('10', 'Heart', 10),
            Card('Jack', 'Heart', 10),
            Card('Queen', 'Heart', 10),
            Card('King', 'Heart', 10),

            Card('Ace', 'Diamond', 1),
            Card('2', 'Diamond', 2),
            Card('3', 'Diamond', 3),
            Card('4', 'Diamond', 4),
            Card('5', 'Diamond', 5),
            Card('6', 'Diamond', 6),
            Card('7', 'Diamond', 7),
            Card('8', 'Diamond', 8),
            Card('9', 'Diamond', 9),
            Card('10', 'Diamond', 10),
            Card('Jack', 'Diamond', 10),
            Card('Queen', 'Diamond', 10),
            Card('King', 'Diamond', 10),

            Card('Ace', 'Club', 1),
            Card('2', 'Club', 2),
            Card('3', 'Club', 3),
            Card('4', 'Club', 4),
            Card('5', 'Club', 5),
            Card('6', 'Club', 6),
            Card('7', 'Club', 7),
            Card('8', 'Club', 8),
            Card('9', 'Club', 9),
            Card('10', 'Club', 10),
            Card('Jack', 'Club', 10),
            Card('Queen', 'Club', 10),
            Card('King', 'Club', 10)
        ]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if self.cards_left() == 0:
            raise Exception('No cards left')
        card = self.cards.pop()
        return card

    def cards_left(self):
        return len(self.cards)
