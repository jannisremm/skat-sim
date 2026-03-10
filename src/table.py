"""This class handles the cards when they are not in the hands of the players"""

import random

from cards import create_deck
from player import Player


class Table:
    def __init__(self) -> None:
        self.skat = []
        self.current_hand = []
        self.trump_suite = None

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

    def start_game(self, player1: Player, player2: Player, player3: Player):
        chosen_player = random.choice([player1, player2, player3])
        chosen_player.take_skat(self.skat)
        self.skat = []
        self.trump_suite = chosen_player.determimne_trump_suit()

    def play_round(self, player1: Player, player2: Player, player3: Player):
        self.current_hand = []
        self.current_hand.append(
            (player1.name, player1.play_card(self.current_hand, self.trump_suite))
        )
        self.current_hand.append(
            (player2.name, player2.play_card(self.current_hand, self.trump_suite))
        )
        self.current_hand.append(
            (player3.name, player3.play_card(self.current_hand, self.trump_suite))
        )

        # evaluate which player has won the trick
        """Pseudocode:
        if one or more players have played a trump card:
            highest trump card wins
        else:
            highest played card of the suit of the first played card wins"""
