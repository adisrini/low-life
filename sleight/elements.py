from enum import Enum

class Suit(Enum):
    CLUB = 1
    HEART = 2
    SPADE = 3
    DIAMOND = 4

class Value(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class Card:
    def __init__(self, suit : Suit, value : Value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return str(self.value.name) + "/" + str(self.suit.name)

    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value
