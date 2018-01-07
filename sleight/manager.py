from sleight.elements import *

class DeckManager:

    def __init__(self):
        self.cards_by_suit = {}
        self.cards_by_value = {}
        self.cards_set = set()

    def add(self, suit : Suit, value : Value):
        if(not suit in self.cards_by_suit):
            self.cards_by_suit[suit] = set()
        if(not value in self.cards_by_value):
            self.cards_by_value[value] = set()

        self.cards_by_suit[suit].add(value)
        self.cards_by_value[value].add(suit)
        self.cards_set.add((suit, value))

    def add_all(self):
        for suit in [Suit.CLUB, Suit.HEART, Suit.SPADE, Suit.DIAMOND]:
            for value in [Value.ACE, Value.TWO, Value.THREE, Value.FOUR, Value.FIVE, Value.SIX, Value.SEVEN, Value.EIGHT, Value.NINE, Value.TEN, Value.JACK, Value.QUEEN, Value.KING]:
                self.add(suit, value)

    def exists(self, suit: Suit, value : Value):
        return not(suit not in self.cards_by_suit or value not in self.cards_by_value or value not in self.cards_by_suit[suit] or suit not in self.cards_by_value[value] or (suit, value) not in self.cards_set)

    def remove(self, suit : Suit, value : Value):
        if not self.exists(suit, value):
            raise Exception

        self.cards_by_suit[suit].remove(value)
        self.cards_by_value[value].remove(suit)
        self.cards_set.remove((suit, value))

    def num_cards(self):
        return len(self.cards_set)

    def num_cards_by_suit(self, suit : Suit):
        return len(self.cards_by_suit[suit])

    def num_cards_by_value(self, value : Value):
        return len(self.cards_by_value[value])
