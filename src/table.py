"""This class handles the cards when they are not in the hands of the players"""

import random

from cards import create_deck
from player import Player


class Table:
    def __init__(self) -> None:
        self.skat = []
        self.current_hand = []

    def shuffle_cards(self):
        """shuffles the list of cards"""
        pass

    def deal_cards(self, player1: Player, player2: Player, player3: Player):
        """Deals the cards to the three players and the skat to the table"""
        cards = create_deck()
        random.shuffle(cards)
        for player in [player1, player2, player3]:
            for _ in range(3):
                player.cards.append(cards.pop())
        self.skat.append(cards.pop())
        self.skat.append(cards.pop())
        for player in [player1, player2, player3]:
            for _ in range(4):
                player.cards.append(cards.pop())
        for player in [player1, player2, player3]:
            for _ in range(3):
                player.cards.append(cards.pop())
