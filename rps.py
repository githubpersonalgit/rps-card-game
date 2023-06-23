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
        self._hand = {}
        self._discard_pile = []
        self._board = ["*", ".", ".", ".", "*"]
        self._played_cards = {}
        Player.all_players.append(self)

    def create_starter_deck(self):
        """Creates a starter deck for all players."""
        starter_deck = {
            "pebble 1": Card("pebble 1", 1, 3, "rock"),
            "pebble 2": Card("pebble 2", 2, 2, "rock"),
            "pebble 3": Card("pebble 3", 4, 3, "rock"),
            "pebble 4": Card("pebble 4", 3, 2, "rock"),
            "pebble 5": Card("pebble 5", 2, 3, "rock"),
            "safety scissors 1": Card("safety scissors 1", 4, 1, "scissors"),
            "safety scissors 2": Card("safety scissors 2", 3, 2, "scissors"),
            "safety scissors 3": Card("safety scissors 3", 5, 1, "scissors"),
            "safety scissors 4": Card("safety scissors 4", 4, 3, "scissors"),
            "safety scissors 5": Card("safety scissors 5", 3, 1, "scissors"),
            "sticky note 1": Card("sticky note 1", 1, 3, "paper"),
            "sticky note 2": Card("sticky note 2", 2, 4, "paper"),
            "sticky note 3": Card("sticky note 3", 1, 5, "paper"),
            "sticky note 4": Card("sticky note 4", 2, 3, "paper"),
            "sticky note 5": Card("sticky note 5", 1, 4, "paper"),
        }

        return starter_deck

    def get_name(self):
        """Rerturns the player's name."""
        return self._name

    def get_deck(self):
        """Returns the player's deck."""
        return self._deck

    def get_board(self):
        """Returns the player's board."""
        return self._board

    def set_deck(self, deck):
        """Sets the player's deck to a new deck."""
        self._deck = deck

    def get_hand(self):
        """Returns the player's hand."""
        return self._hand

    def set_hand(self, hand):
        """Sets players' hand"""
        self._hand = hand

    def get_played_cards(self):
        """Returns the player's played cards."""
        return self._played_cards


class Card:
    """Represents a card for the rock, papers, scissors card game.
    It has a suit, attack and defense stats"""

    def __init__(self, name, attack, defense, suit):
        """Initializes a card with the given name, attack, defense and suit."""
        self._name = name
        self._attack = attack
        self._defense = defense
        self._suit = suit
        self._front = (suit, attack, defense)
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
        self._first_round = True
        self._list_of_players = Player.all_players

    def shuffle_starter_decks(self):
        """Shuffles each player's deck at the beginning of the game."""
        for player in self._list_of_players:
            # makes a list of tuples with card name(key) : card object(value) pairs
            list_of_values = list(player.get_deck().items())
            random.shuffle(list_of_values)
            # shuffles the player's deck
            shuffled_starter_deck = dict(list_of_values)
            player.set_deck(shuffled_starter_deck)

    def get_list_of_players(self):
        """Returns the list of players playing the game."""
        return self._list_of_players

    def shuffle_discard_pile(self, discard_pile, player):
        """Shuffle the	discard pile and makes a new draw deck for the player."""

    def start_round(self):
        """Sets a new round."""
        # if it's the first round, shuffle the starter decks
        if self._first_round:
            self.shuffle_starter_decks()
            self._first_round = False
        self.draw_cards()

    def play_card(self, player_object):
        """Prompts the player to choose a card and position to play."""
        card_to_play = input(
            f"{player_object.get_name()}, enter name of the card to play: "
        )
        position = input(
            f"{player_object.get_name()}, enter position to play the chosen card: "
        )
        self.execute_play_card(player_object, card_to_play, int(position))

    def execute_play_card(self, player_object, card_name, position):
        """Places the player's selected card from their hand on the specified position."""
        if player_object.get_name() in (
            "player1",
            "player 1",
            "Player 1",
            "Player1",
            "player 2",
            "player2",
            "Player 2",
            "Player2",
        ):
            # checks if the card is in the player's hand
            if card_name in player_object.get_hand():
                # sets the selected position to the selcted card's back side
                player_object.get_board()[position] = player_object.get_hand()[
                    card_name
                ].get_back_side()
                # adds the played card to that player's played cards dictionary(position : card_object)
                player_object.get_played_cards()[
                    position
                ] = player_object.get_hand().pop(card_name)

    def reveal_board_cards(self):
        """Reveals cards on all players' boards."""
        for player in self._list_of_players:
            # checks the position of every played card in the player's board
            for position, card_in_position in enumerate(player.get_board()):
                # checks if the card in that position is not revealed
                if card_in_position == "X":
                    # reveals the card on that position
                    player.get_board()[position] = player.get_played_cards()[
                        position
                    ].get_front_side()

    def confirm_values(self, player):
        """Confirms the player's played values."""

    def draw_cards(self):
        """Players draw the first five values from their deck to their hand."""
        for player in self._list_of_players:
            cards_to_remove_from_deck = dict(list(player.get_deck().items())[:5])
            dictionary_of_drawn_cards = dict(cards_to_remove_from_deck)
            player.set_hand(dictionary_of_drawn_cards)
            for card in cards_to_remove_from_deck:
                del player.get_deck()[card]

    def discard_values(self, player):
        """Allows the player to discard values from their hand."""


game = RPS()
p1 = Player("Player 1")
p2 = Player("Player 2")
game.shuffle_starter_decks()
print("Player 1 deck: ")
for card in p1.get_deck().values():
    print(card.get_name())
print("")
print("Player 2 deck: ")
for card in p2.get_deck().values():
    print(card.get_name())
print("")
game.draw_cards()
for player in game.get_list_of_players():
    print(player.get_name() + " hand")
    for card in player.get_hand().values():
        print(card.get_name())
    print("")
print("Player 1 deck: ")
for card in p1.get_deck().values():
    print(card.get_name())
print("")
print("Player 2 deck: ")
for card in p2.get_deck().values():
    print(card.get_name())
print("")
game.play_card(p1)
game.reveal_board_cards()
print("")
print("This player 1's current board: ")
print(p1.get_board())
print("")
game.play_card(p2)
game.reveal_board_cards()
print("This player 2's current board: ")
print("")
print(p2.get_board())
print("")
