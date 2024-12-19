
class Card:

    def __init__(self, value, suit):
        """Attributes: value (2-14, 14 is Ace), suit (1-4)"""
        if type (value) != int:
            raise TypeError ("value type must be int! ")

        if type (suit) != int:
            raise TypeError ("suit type must be int")

        if value < 2 or value > 14:
            raise ValueError ("Invalid value: must be an integer between 2 and 14.")

        if suit < 1 or suit > 4:
            raise ValueError ("invalid suit, suit must be from 1-4")

        self.value = value
        self.suit = suit

    # A dictionary that maps numeric values to their values names
    VALUES_DICT = {2 : "2", 3: "3", 4: "4", 5 : "5", 6 : "6", 7 : "7",
                   8 : "8", 9 : "9" , 10 : "10", 11 : "Jack", 12 : "Queen",
                   13: "King", 14 : "Ace"}

    # A dictionary that maps numeric suit to their suit names
    SUIT_DICT = {1 : "Diamond ♦️" ,2 : "Spade ♠️",
                 3 : "Heart ♥️", 4 : "Club ♣️"}

    def __repr__(self):
        """Returns a string representation of the card"""
        return f"{self.VALUES_DICT[self.value] + " " + self.SUIT_DICT[self.suit]}"


    def __gt__(self, other):
        """Compare cards by value, if values are equal, compare by suit"""
        if type(other) != Card:
            raise TypeError("Other type must be class Card! 🃏")

        if self.value == other.value:
            return self.suit > other.suit

        else:
            return self.value > other.value

    def __eq__(self, other):
        """Checks if two cards are equal based on their value and suit"""
        if type(other) != Card:
            raise TypeError("Other type must be class Card! 🃏")

        return self.value == other.value and self.suit == other.suit

