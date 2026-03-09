from dataclasses import dataclass


@dataclass(frozen=True)
class Card:
    """This class is used to represent a single card

    Returns:
        string: suit and rank of the card
    """

    suit: str
    rank: str
    points: int

    def __repr__(self):
        return f"{self.suit} {self.rank}"


SUITS = ["Eichel", "Grün", "Herz", "Schell"]
RANKS = ["Ass", "Zehn", "König", "Ober", "Unter", "Neun", "Acht", "Sieben"]
POINT_VALUES = {
    "Ass": 11,
    "Zehn": 10,
    "König": 4,
    "Ober": 3,
    "Unter": 2,
    "Neun": 0,
    "Acht": 0,
    "Sieben": 0,
}


def create_deck():
    return [Card(suit, rank, POINT_VALUES[rank]) for suit in SUITS for rank in RANKS]
