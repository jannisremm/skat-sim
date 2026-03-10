"""This class defines the players, the cards in their hands and total points, and the actions they can take"""

import random

from cards import SUITS


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.cards = []
        self.points = 0
        self.won_tricks = []

    def play_card(self, cards_on_table, trump_suite):
        """Choses the best available legal card to play
        currently uses random logic"""
        if len(cards_on_table) == 0:
            # The first card that is played can be random
            card_to_play = self.cards.pop()
            return card_to_play

        # The second and third players need to follow suit
        suit_to_follow = cards_on_table[0][1].suit
        legal_cards = [card for card in self.cards if card.suit == suit_to_follow]
        if legal_cards:
            card_to_play = legal_cards.pop()
            self.cards.remove(card_to_play)
        else:
            card_to_play = self.cards.pop()

        return card_to_play

    def take_skat(self, skat):
        for card in skat:
            self.cards.append(card)
        random.shuffle(self.cards)
        own_cards = []
        own_cards.append(self.cards.pop())
        own_cards.append(self.cards.pop())
        self.won_tricks.append((own_cards))

    def determimne_trump_suit(self):
        return random.choice(SUITS)
