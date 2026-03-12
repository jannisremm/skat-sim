"""This class handles the cards when they are not in the hands of the players"""

import random

from cards import RANKS, create_deck
from player import Player


class Table:
    def __init__(self, players) -> None:
        self.players = players
        self.skat = []
        self.current_hand = []
        self.trump_suite = None
        self.current_game_value = 0

    def shuffle_cards(self):
        """shuffles the list of cards"""
        pass

    def deal_cards(self):
        """Deals the cards to the three players and the skat to the table"""
        cards = create_deck()
        random.shuffle(cards)
        for player in self.players:
            for _ in range(3):
                player.cards.append(cards.pop())
        self.skat.append(cards.pop())
        self.skat.append(cards.pop())
        for player in self.players:
            for _ in range(4):
                player.cards.append(cards.pop())
        for player in self.players:
            for _ in range(3):
                player.cards.append(cards.pop())

        for player in self.players:
            player.remember_cards()

    def start_game(self):
        for player in self.players:
            player.current_game_team = ""
            player.won_tricks = []
        chosen_player = random.choice(self.players)
        print("Player chosen to chose trump suit:", chosen_player.name)
        chosen_player.take_skat(self.skat)
        self.skat = []
        self.trump_suite = chosen_player.determine_trump_suit()
        print("Chosen trump suit:", self.trump_suite)
        chosen_player.current_game_team = "Re"

    def play_round(self):
        self.current_hand = []
        self.current_hand.append(
            (
                self.players[0],
                self.players[0].play_card(self.current_hand, self.trump_suite),
            )
        )
        self.current_hand.append(
            (
                self.players[1],
                self.players[1].play_card(self.current_hand, self.trump_suite),
            )
        )
        self.current_hand.append(
            (
                self.players[2],
                self.players[2].play_card(self.current_hand, self.trump_suite),
            )
        )

        # evaluate which player has won the trick
        """Pseudocode:
        if one or more players have played a trump card:
            highest trump card wins
        else:
            highest played card of the suit of the first played card wins"""
        # print("Current hand:", self.current_hand)
        suit_to_follow = self.current_hand[0][1].suit
        # print("Suit to follow:", suit_to_follow)
        current_winner = self.current_hand[0]

        # check if the suit is correct
        if self.current_hand[1][1].suit == suit_to_follow:
            # check if the rank of the card is higher (earlier in the list of ranks)
            if RANKS.index(self.current_hand[1][1].rank) < RANKS.index(
                current_winner[1].rank
            ):
                current_winner = self.current_hand[1]
        if self.current_hand[2][1].suit == suit_to_follow:
            if RANKS.index(self.current_hand[2][1].rank) < RANKS.index(
                current_winner[1].rank
            ):
                current_winner = self.current_hand[2]

        current_winner[0].won_tricks.append(
            [self.current_hand[0][1], self.current_hand[1][1], self.current_hand[2][1]]
        )
        # print("Winner of the trick:", current_winner[0])
        # print("Winning card: ", current_winner[1])
        # print("Tricks won by current winner: ", current_winner[0].won_tricks)

        """Change the player order, so the player that won the trick plays first next round"""
        winner_position = self.players.index(current_winner[0])
        # print("Current order:", self.players)
        # print("Winner position: ", winner_position)
        self.players = self.players[winner_position:] + self.players[:winner_position]
        # print("new order:", self.players)

    def determine_round_winner(self):
        re_team = next(
            player for player in self.players if player.current_game_team == "Re"
        )
        contra_team = [player for player in self.players if player is not re_team]

        re_team_points = re_team.get_game_points()
        contra_team_points = sum(player.get_game_points() for player in contra_team)
        print("Re:", re_team_points, re_team.name)

        print("Contra:", contra_team_points)
        print(contra_team[0].get_game_points(), contra_team[0].name)
        print(contra_team[1].get_game_points(), contra_team[1].name)

        bonus_multiplier = 0
        if re_team_points in (0, 120):
            bonus_multiplier += 2
        elif re_team_points >= 90 or re_team_points <= 30:
            bonus_multiplier += 1

        self.current_game_value = re_team.determine_game_value(bonus_multiplier)

        print("Game value:", self.current_game_value)
        if re_team_points > 60:
            print("Re team has won")
            re_team.total_points += self.current_game_value
            print(re_team, "gains", self.current_game_value)
        else:
            print("Contra team has won")
            re_team.total_points -= 2 * self.current_game_value
            print(re_team, "loses", 2 * self.current_game_value)

    def determine_total_winner(self):
        players = self.players
        ranking = sorted(players, key=lambda player: player.total_points, reverse=True)  # type: ignore
        print("First place:\t", ranking[0], "\t", ranking[0].total_points)
        print("Second place:\t", ranking[1], "\t", ranking[1].total_points)
        print("Third place:\t", ranking[2], "\t", ranking[2].total_points)


if __name__ == "__main__":
    horst = Player("Horst")
    ulf = Player("Ulf")
    gunni = Player("Gunni")

    tisch = Table([horst, ulf, gunni])

    for _ in range(9):
        tisch.deal_cards()
        tisch.start_game()
        for _ in range(10):
            tisch.play_round()
        tisch.determine_round_winner()
        tisch.determine_total_winner()
