"""This file handles the game flow, determines which players turn it is etc, and calculates points at the end"""

from player import Player
from table import Table

horst = Player("Horst")
ulf = Player("Ulf")
gunni = Player("Gunni")

tisch = Table()

tisch.deal_cards(horst, ulf, gunni)

print(horst.cards)
print(ulf.cards)
print(gunni.cards)
print(tisch.skat)
