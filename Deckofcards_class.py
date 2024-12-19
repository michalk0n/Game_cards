from Card_class import Card
from random import shuffle, choice


class DeckOfCard:
    def __init__(self):
        """Attributes: list of 52 different cards"""
        self.cards_list =[]
        # Create a list of cards with all possible combinations of value (2-14) and suit (1-4)
        for value in range(2,15):
            for suit in range(1,5):
                self.cards_list.append(Card(value, suit))


    def card_shuffle(self):
        """Shuffle the deck of cards"""

        if not self.cards_list:  #if the list is empty nothing changes
            self.cards_list = []

        list_before_shuffle = self.cards_list[:]  # Save a copy of the current order
        shuffle(self.cards_list)  #shuffle

        if list_before_shuffle == self.cards_list:  # Verify if the order has changed
            shuffle(self.cards_list)   # if not shuffle again

    def deal_one(self):
        """Picking and removing a random card from the list
        and returning it"""

        if not self.cards_list: # Raises an exception if the deck is empty
            raise ValueError("Cannot deal from an empty deck!")

        card = choice(self.cards_list)
        self.cards_list.remove(card)
        return card

    def __repr__(self):
        """Return a string representation of the deck."""
        return f"There's are {len(self.cards_list)} left in your deck of cards"

