from Deckofcards_class import DeckOfCard
from Player_class import Player

class CardGame:

    def __init__(self, name1, name2, cards_amount1 = 26, cards_amount2 = 26):
        """Initialize two players and the game deck of cards"""
        if type(name1) != str or type(name2) != str:
            raise TypeError("Name type must be a string! ")

        if name2 == name1:  # Avoiding two players with same name
            name2 += "2"

        if type(cards_amount1) != int or type(cards_amount2) != int:
            raise TypeError("Cards amount type must be int! ")

        if cards_amount1 < 10 or cards_amount1 > 26:
            cards_amount1 = 26

        if cards_amount2 < 10 or cards_amount2 > 26:
            cards_amount2 = 26    # default to 26 cards if not within valid range

        self.player1 = Player(name1, cards_amount1)
        self.player2 = Player(name2, cards_amount2)
        self.deck_of_cards = DeckOfCard()
        self.initialized = False # A flag to track the object initialization
        self.new_game()
        self.initialized = True # Set the flag to True after new_game has been called

    def new_game(self):
        """Shuffle the deck and set hands for both players
        This method can only be called once during initialization"""

        if not self.initialized:    # Check if new_game is being called from __init__
            # Shuffle the deck and set hands for both players
            self.deck_of_cards.card_shuffle()
            self.player1.set_hand(self.deck_of_cards)
            self.player2.set_hand(self.deck_of_cards)
        else:
            print("new_game can be called only from __init__")

    def get_winner(self):
        """Determine the winner based on the number of cards each player has
        if it's a tie, return None"""

        if  len(self.player1.cards_list) == len(self.player2.cards_list):
            return None   # Tie

        elif len(self.player1.cards_list) > len(self.player2.cards_list):
            return self.player1   # Player 1 wins

        else:
            return self.player2   # Player 2 wins




