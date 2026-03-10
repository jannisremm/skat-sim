"""This class defines the players, the cards in their hands and total points, and the actions they can take"""


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.cards = []
        self.points = 0

    def play_card(self, cards_on_table):
        """Choses the best available legal card to play
        currently uses random logic"""
        if len(cards_on_table) == 0:
            # The first card that is played can be random
            card_to_play = self.cards.pop()
            return card_to_play

        # The second and third players need to follow suit
        suit_to_follow = cards_on_table[0].suit
        legal_cards = [card for card in self.cards if card.suit == suit_to_follow]
        if legal_cards:
            card_to_play = legal_cards.pop()
            self.cards.remove(card_to_play)
        card_to_play = self.cards.pop()

        return card_to_play
