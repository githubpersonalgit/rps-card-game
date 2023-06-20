# Author: Josue Alamo
# Date: 06/16/23
# Description:


import random


class Player:
    """Represents a human player."""

    all_players = []

    def __init__(self, name):
        self._name = name
        self._deck = self.create_starter_deck()
        self._hand = []
        self._discard_pile = []
        Player.all_players.append(self)

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
        self._suit = suit
        self._front = suit
        self._back = "X"
        self._face = self._back

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
        return self._suit

    def get_back_side(self):
        """Returns the card's back side."""
        return self._back

    def get_front_side(self):
        """Returns the card's front side."""
        return self._front

    def get_face(self):
        """Returns the card's face."""
        return self._face


class RPS:
    """Represents the rock, papers, scissors game."""

    def __init__(self):
        """Initializes the game with the given player 1 and player 2 boards."""
        self._player1_board = ["*", ".", ".", ".", "*"]
        self._player2_board = ["*", ".", ".", ".", "*"]
        self._first_round = True
        self._list_of_players = Player.all_players

    def get_player1_board(self):
        """Returns the player 1's board."""
        return self._player1_board

    def get_player2_board(self):
        """Returns the player 2's board."""
        return self._player2_board

    def shuffle_starter_decks(self):
        """Shuffles each player's deck at the beginning of the game."""
        for player in self._list_of_players:
            random.shuffle(player.get_deck())

    def shuffle_discard_pile(self, discard_pile, player):
        """Shuffle the	discard pile and makes a new draw deck for the player."""

    def start_round(self):
        """Sets a new round."""
        # if it's the first round, shuffle the starter decks
        if self._first_round:
            self.shuffle_starter_decks()
            self._first_round = False
        self.draw_cards()

    def play_card(self, player, card, position):
        """Allows the player to play a card from their hand on the specified position."""
        # Play a card face down on the player's board
        if player == "player 1" or "PLayer 1":
            self._player1_board[position] = card.get_back_side()
        if player == "player 2" or "Player 2":
            self._player2_board[position] = card.get_back_side()

    def confirm_cards(self, player):
        """Confirms the player's played cards."""

    def draw_cards(self):
        """Players draw the first five cards from their deck to their hand."""
        for player in self._list_of_players:
            while len(player.get_hand()) < 5:
                player.get_hand().append(player.get_deck().pop(0))

    def discard_cards(self, player):
        """Allows the player to discard cards from their hand."""


game = RPS()
p1 = Player("Player 1")
p2 = Player("Player 2")
game.shuffle_starter_decks()
print("Player 1 deck: ")
for card in p1.get_deck():
    print(card.get_name())
print("")
print("Player 2 deck: ")
for card in p2.get_deck():
    print(card.get_name())
print("")
game.draw_cards()
for player in game._list_of_players:
    print(player.get_name())
    for card in player.get_hand():
        print(card.get_name())
    print("")
for player in game._list_of_players:
    print(player.get_name())
    for card in player.get_deck():
        print(card.get_name())
    print("")
