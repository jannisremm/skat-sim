"""This class defines the players, the cards in their hands and total points, and the actions they can take"""

import random

from cards import SUITS


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.cards = []
        self.total_points = 0
        self.won_tricks = []
        self.current_game_team = ""

    def __repr__(self) -> str:
        # needs to be extended to fully represent the class
        return self.name

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

    def determine_trump_suit(self):
        suit_counts = {suit: 0 for suit in SUITS}
        for card in self.cards:
            if card.rank == "Unter":
                continue
            suit_counts[card.suit] += 1
        return max(suit_counts, key=suit_counts.get)  # type: ignore

    def determine_game_value(self):
        """Determine count and order of Unter"""
        unter_suits = {card.suit for card in self.cards if card.rank == "Unter"}
        print(unter_suits)
        count = 0
        if SUITS[0] in unter_suits:
            for suit in SUITS:
                if suit in unter_suits:
                    count += 1
                else:
                    break
        else:
            for suit in SUITS:
                if suit not in unter_suits:
                    count += 1
                else:
                    break
        trump_suit = self.determine_trump_suit()
        suit_multipliers = {SUITS[0]: 12, SUITS[1]: 11, SUITS[2]: 10, SUITS[3]: 9}
        return suit_multipliers[trump_suit] * (count + 1)

    def get_game_points(self):
        points = 0
        for trick in self.won_tricks:
            for card in trick:
                points += card.points
        return points
