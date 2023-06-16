# Author: Josue Alamo
# Date: 06/16/23
# Description:


class Player:
    """Represents a human player."""

    def __init__(self, name):
        self._name = name
        self._deck = []
        self._hand = []

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
        """Returns the card's attack."""
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
