# Author: Josue Alamo
# Date: 06/16/23
# Description:


import random


class Player:
    """Represents a human player."""

    def __init__(self, name):
        self._name = name
        self._deck = self.create_starter_deck()
        self._hand = []
        self._discard_pile = []

    def create_starter_deck(self):
        """Creates a starter deck for all players."""
        card1 = Card("pebble1", 1, 3, "rock")
        card2 = Card("pebble2", 2, 2, "rock")
        card3 = Card("pebble3", 4, 3, "rock")
        card4 = Card("pebble4", 3, 2, "rock")
        card5 = Card("pebble5", 2, 3, "rock")
        card6 = Card("safety scissors1", 4, 1, "scissors")
        card7 = Card("safety scissors2", 3, 2, "scissors")
        card8 = Card("safety scissors3", 5, 1, "scissors")
        card9 = Card("safety scissors4", 4, 3, "scissors")
        card10 = Card("safety scissors5", 3, 1, "scissors")
        card11 = Card("sticky note1", 1, 3, "paper")
        card12 = Card("sticky note2", 2, 4, "paper")
        card13 = Card("sticky note3", 1, 5, "paper")
        card14 = Card("sticky note4", 2, 3, "paper")
        card15 = Card("sticky note5", 1, 4, "paper")
        starter_deck = [
            card1,
            card2,
            card3,
            card4,
            card5,
            card6,
            card7,
            card8,
            card9,
            card10,
            card11,
            card12,
            card13,
            card14,
            card15,
        ]

        return starter_deck

    def get_name(self):
        """Rerturns the player's name."""
        return self._name

    def get_deck(self):
        """Returns the player's deck."""
        return self._deck

    def get_hand(self):
        """Returns the player's hand."""
        return self._hand


class Card:
    """Represents a card for the rock, papers, scissors card game.
    It has a suit, attack and defense stats"""

    def __init__(self, name, attack, defense, suit):
        """Initializes a card with the given name, attack, defense and suit."""
        self._name = name
        self._attack = attack
        self._defense = defense
        self.__suit = suit

    def get_name(self):
        """Returns the card's name."""
        return self._name

    def get_attack(self):
        """Returns card's attack."""
        return self._attack

    def get_defense(self):
        """Returns the card's defense."""
        return self._defense

    def get_suit(self):
        """Returns the card's suit."""
        return self.__suit


class RPS:
    """Represents the rock, papers, scissors game."""

    def __init__(self):
        """Initializes the game with the given player 1 and player 2 boards."""
        self._player1_board = ["*", ".", ".", ".", "*"]
        self._player2_board = ["*", ".", ".", ".", "*"]

    def get_player1_board(self):
        """Returns the player 1's board."""
        return self._player1_board

    def get_player2_board(self):
        """Returns the player 2's board."""
        return self._player2_board

    def shuffle_starter_deck(self, starter_deck):
        """Shuffles each player's deck at the beginning of the game."""
    
    def shuffle_discard_pile(self, discard_pile, player):
        """Shuffle the	discard pile and makes a new draw deck for the player."""

    def play_game(self, player):
        """Allows the player to play the game and place cards on the board."""

    def confirm_cards(self, player):
        """Confirms the player's played cards."""

    def draw_cards(self, player):
        """Acardlows the player to draw cards from their deck."""
        for card in range(5):
            player.get_hand().append(player.get_deck().pop(card))

    def discard_cards(self, player):
        """Allows the player to discard cards from their hand."""


game = RPS()
p1 = Player("Player 1")
p2 = Player("Player 2")

