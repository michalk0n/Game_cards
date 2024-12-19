from Deckofcards_class import DeckOfCard
from Card_class import Card
from random import choice

class Player:

    def __init__(self, player_name, cards_amount = 26):
        """Attributes: player name, card amount: default is 26
        and an empty cards list"""

        if type(player_name) != str:
            raise TypeError("player name type must be string !")

        if len(player_name) < 1 :
            raise ValueError("Name cant be empty! ")

        if len(player_name) > 15:
            player_name = player_name[:16]

        if type(cards_amount) != int:
            raise TypeError("cards amount type must be int  from 10-26")

        if cards_amount < 10 or cards_amount > 26:
            cards_amount = 26   # default to 26 cards if not within valid range

        self.player_name = player_name
        self.card_amount = cards_amount
        self.cards_list = []

    def set_hand(self, deck_of_cards):
        """ Assigns random cards from the deck to the players card list
        according to his amount"""

        if type(deck_of_cards) != DeckOfCard:
            raise TypeError("Deck of card type must be DeckOfCard")

        # If there's not enough cards in the deck, we deal as much as we can
        if len(deck_of_cards.cards_list) < self.card_amount:
            self.card_amount = len(deck_of_cards.cards_list)

        for i in range(self.card_amount):   # Deal the cards to the player
            self.cards_list.append(deck_of_cards.deal_one())


    def get_card(self):
        """Picking and removing a random card from the list
        and returning it"""
        if not self.cards_list:  # Return None if the player hand is empty
            return None

        card = choice(self.cards_list)
        self.cards_list.remove(card)
        return card


    def add_card(self, card):
        """Adds a card to the player's hand if it's not already exists"""
        if type(card) != Card:
            raise TypeError ("Card type must be Card! ")

        if card  not in self.cards_list:  # Check for duplicate cards
            self.cards_list.append(card)

    def __repr__(self):
        """Returns the player's name and the number of cards they have"""
        return f"Player {self.player_name} has {len(self.cards_list)} cards: {self.cards_list}"


