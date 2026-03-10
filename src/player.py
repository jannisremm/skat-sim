"""This class defines the players, the cards in their hands and total points, and the actions they can take"""


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.cards = []
        self.points = 0

    def play_card(self):
        """Choses the best available legal card to play"""
        pass
