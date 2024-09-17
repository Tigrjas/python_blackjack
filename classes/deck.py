
import itertools
import random


class Deck:
    vals = ['2', '3', '4', '5', '6', '7', '8',
            '9', '10', 'jack', 'queen', 'king', 'ace']

    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    deck = list(itertools.product(vals, suits))

    def __init__(self):
        self.shuffle_deck()

    def remove_card(self):
        return self.deck.pop()

    def reset_deck(self):
        self.deck = list(itertools.product(vals, suits))

    def print_deck(self):
        for val, suit in self.deck:
            print('The %s of %s' % (val, suit))

    def shuffle_deck(self):
        random.shuffle(self.deck)
