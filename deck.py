import random
import copy

class Deck:
    '''
    This class represents a deck of cards
    the deck will be automatically shuffled upon creation

    The deck also has a card class which represents individual cards in a deck
    '''

    class Card:
        def __init__(self, rank, suit):
            self.rank = rank
            self.suit = suit

        def get_rank(self):
            return self.rank

        def get_suit(self):
            return self.suit

    RANKS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
             'A': 14}

    deck = []
    full_deck = []

    def __init__(self):
        for RANK in self.RANKS.keys():
            self.deck.append(Deck.Card(RANK, 'red hearts'))
            self.deck.append(Deck.Card(RANK, 'red diamonds'))
            self.deck.append(Deck.Card(RANK, 'black clubs'))
            self.deck.append(Deck.Card(RANK, 'black spades'))

        random.shuffle(self.deck)

        # create an extra deck to refill the main deck
        self.replacement_deck = copy.deepcopy(self.deck)

    def reshuffle(self):
        self.deck = copy.deepcopy(self.replacement_deck)
        random.shuffle(self.deck)

    def draw(self):
        return self.deck.pop()
