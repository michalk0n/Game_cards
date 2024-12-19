from unittest import TestCase
from unittest import mock
from unittest.mock import patch
from Deckofcards_class import DeckOfCard
from Card_class import Card


class TestDeckOfCard(TestCase):

    def setUp(self):
        """initialization of deck of cards"""
        self.deck_of_cards1 = DeckOfCard()

    # ---- Test init ----

    def test_init_valid_52_cards(self):
        """Test that the deck contains exactly 52 cards after initialization"""
        self.assertEqual(52, len(self.deck_of_cards1.cards_list))

    def test_init_valid_card_list(self):
        """Test that the cards_list attribute is of type list"""
        self.assertEqual(list, type(self.deck_of_cards1.cards_list))

    def test_init_valid_Card(self):
        """Test that all valid values and suits Card combination are in deck"""
        cards = [Card(value, suit) for value in range(2,14) for suit in range(1,4)]
        for card in cards:
            self.assertIn(card, self.deck_of_cards1.cards_list)

    # ----- Test shuffle -----

    def test_card_shuffle_valid_order_changed(self):
        """Test that shuffling the deck changes the order of the cards"""
        original_deck = self.deck_of_cards1.cards_list[:]  # Save a copy of the current order
        self.deck_of_cards1.card_shuffle()
        self.assertNotEqual(original_deck, self.deck_of_cards1.cards_list)

    def test_card_shuffle_empty_deck(self):
        """Test that trying to shuffle an empty return an empty deck"""
        self.deck_of_cards1.cards_list = []  # Empty the deck
        self.assertEqual([], self.deck_of_cards1.cards_list)

    # -----Test deal_one----
    def test_deal_one_valid_one_delete(self):
        """Test that dealing one card reduces the deck size by one"""
        self.deck_of_cards1.deal_one()
        self.assertEqual(51, len(self.deck_of_cards1.cards_list))

    def test_deal_one_valid_return_Card(self):
        """Test that the return card is type Card"""
        card = self.deck_of_cards1.deal_one()
        self.assertEqual(Card, type(card))

    def test_deal_one_valid_card_from_list(self):
        """Test that the card that got deleted is from the original deck"""
        original_list = self.deck_of_cards1.cards_list[:]
        self.assertIn(self.deck_of_cards1.deal_one(), original_list)

    def test_deal_one_valid_card_not_in_list(self):
        """Test that the card is not in the deck"""
        card = self.deck_of_cards1.deal_one()
        self.assertNotIn(card, self.deck_of_cards1.cards_list)

    def test_deal_one_invalid_empty_desk(self):
        """Test that attempting to deal a card from an empty deck raises a ValueError"""
        with self.assertRaises(ValueError):
            self.deck_of_cards1.cards_list = []
            self.deck_of_cards1.deal_one()

