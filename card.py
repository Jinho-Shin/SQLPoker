
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
rank_values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
               'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self, suit, rank):
        if (suits.count(suit) == 0):
            raise Exception('Undefined Suit')
        self.suit = suit
        if (ranks.count(rank) == 0):
            raise Exception('Undefined Rank')
        self.rank = rank
        self.rank_value = rank_values[rank]
        self.is_ace = self.rank == 'Ace'

    def __str__(self):
        return self.rank + '(' + str(self.rank_value) + ') of ' + self.suit

class Deck:
    def __init__(self):
        self.deck = []
        # deck has all the suits and ranks
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
        


