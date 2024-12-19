from unittest import TestCase
from unittest.mock import patch
from Card_class import Card
from Deckofcards_class import DeckOfCard
from Player_class import Player


class TestPlayer(TestCase):

    def setUp(self):
        """Set up players instances for testing"""
        self.player1 = Player("player1")
        self.player2 =  Player("player2", 10)
        self.player3 = Player("player3")
        self.deck_of_card = DeckOfCard()
        self.player3.set_hand(self.deck_of_card)

    # ----------Test init----------
    def test_init_valid_default_card_amount(self):
        """Test that the player is correctly initialized with default card amount"""
        self.assertEqual(26, self.player1.card_amount)

    def test_init_valid_empty_cards_list(self):
        """Test that the player's initial cards list is empty"""
        self.assertEqual([], self.player1.cards_list)

    def test_init_valid_card_amount_10(self):
        """Test that the player is correctly initialized with edge amount: 10"""
        self.assertEqual(10, self.player2.card_amount)

    def test_init_valid_card_amount_26(self):
        """Test that the player is correctly initialized with edge amount: 26"""
        player = Player("Player", 26)
        self.assertEqual(26, player.card_amount)

    def test_init_card_amount_small_9(self):
        """Test that if the card amount is less than 10, it defaults to 26 cards"""
        player = Player("player", 9)
        self.assertEqual(26, player.card_amount)

    def test_init_card_amount_big_27(self):
        """Test that if the card amount is greater than 26, it defaults to 26 cards"""
        player = Player("player", 27)
        self.assertEqual(26, player.card_amount)

    def test_init_valid_name(self):
        """Test that the player's name is correctly initialized"""
        self.assertEqual("player1", self.player1.player_name)

    def test_init_invalid_name_type(self):
        """Test that a TypeError is raised when the player name is not a string"""
        with self.assertRaises(TypeError):
            Player(562)

    def test_init_invalid_short_name_0(self):
        """Test that a ValueError is raised when the player name is too short (less than 1 character)"""
        with self.assertRaises(ValueError):
            Player("")

    def test_init_invalid_long_name_16(self):
        """Test that a ValueError is raised when the player name is too long (more than 15 characters)"""
        player = Player("abcdefghijklmnop")
        self.assertEqual(player.player_name[:16], player.player_name)

    def test_init_invalid_card_amount_type(self):
        """Test that a TypeError is raised when the card amount is not an integer"""
        with self.assertRaises(TypeError):
            Player("player", "26")


    # -------- Test set_hand ----------
    def test_set_hand_valid_deck_amount(self):
        """Test that there's are correct amount of cards in the list"""
        with patch('Deckofcards_class.DeckOfCard.deal_one') as mock_deal_one:
                mock_deal_one.side_effect = [Card(value, suit) for value in range (2,15) for suit in range (1,5)]
                self.player1.set_hand(self.deck_of_card)
                self.assertEqual(26, len(self.player1.cards_list))


    def test_set_hand_valid_no_duplicates(self):
        """Test that there's are no duplicates in the players card list"""
        with patch('Deckofcards_class.DeckOfCard.deal_one') as mock_deal_one:
            mock_deal_one.side_effect = [(value, suit) for value in range (2,15) for suit in range (1,5)]
            self.player1.set_hand(self.deck_of_card)
            self.assertEqual(26, len(set(self.player1.cards_list)))

    def test_set_hand_valid_cards_removed(self):
        """Test that the cards are not in deck anymore"""
        self.player2.set_hand(self.deck_of_card)
        for card in self.player2.cards_list:
            self.assertNotIn(card, self.deck_of_card.cards_list)


    def test_set_hand_invalid_deck_not_enough(self):
        """Test if player amount is greater than the deck, we set the player all the deck"""
        self.deck_of_card.cards_list = [Card(2, 2), Card(3, 2)]
        self.player1.set_hand(self.deck_of_card)
        self.assertEqual(2, len(self.player1.cards_list))


    def test_set_hand_invalid_deck_type(self):
        """Test that a TypeError is raised when an invalid type (non-DeckOfCard) is passed"""
        with self.assertRaises(TypeError):
            self.player1.set_hand(26)


    # -------Test get card --------

    def test_get_card_valid_one_card_delete(self):
        """Test that when a player gets a card, the card is removed from their hand"""
        self.player3.get_card()
        self.assertEqual(25, len(self.player3.cards_list))

    def test_get_card_valid_card_not_in_list(self):
        """Test that the card is no longer in the player's hand"""
        card = self.player3.get_card()
        self.assertNotIn(card, self.player3.cards_list)

    def test_get_card_valid_card_from_list(self):
        """Test that the card that got deleted is from the original player deck"""
        original_deck = self.player3.cards_list[:]
        card = self.player3.get_card()
        self.assertIn(card, original_deck)

    def test_get_card_valid_type_Card(self):
        """Test that the card returned is of type Card"""
        card = self.player3.get_card()
        self.assertEqual(Card, type(card))

    def test_get_card_invalid_empty_desk(self):
        """Test that the method return None when the player tries to get a card when their hand is empty"""
        self.player3.cards_list = []
        self.assertEqual(None, self.player3.get_card())

    #  --------- Test add card -------

    def test_add_card_valid_card_added(self):
        """Test that one card is added to the player's hand when he already has cards"""
        self.player3.cards_list = [Card(2,2), Card(3,2)]   # helps make sure card is not in list already
        self.player3.add_card(Card(4,2))
        self.assertEqual(3, len(self.player3.cards_list))

    def test_add_card_valid_to_empty_list(self):
        """Test that one card is added to an empty hand"""
        self.player3.cards_list = []
        self.player3.add_card(Card(4,2))
        self.assertEqual(1, len(self.player3.cards_list))

    def test_add_card_valid_card_in_deck(self):
        """Test that the added card is in the player's hand"""
        self.player3.cards_list = [Card(2,2), Card(3,2)]   # helps make sure card is not in list already
        card = Card(4,2)
        self.player3.add_card(card)
        self.assertIn(card, self.player3.cards_list)

    def test_add_card_invalid_duplicate_card(self):
        """Test that when attempting to add a duplicate card to the player's hand the card is not added"""
        self.player3.cards_list = [Card(2, 2), Card(3, 2)]
        self.player3.add_card(Card(2,2))
        self.assertEqual(2, len(self.player3.cards_list))

    def test_add_card_invalid_card_type(self):
        """Test that a TypeError is raised when attempting to add not a Card"""
        with self.assertRaises(TypeError):
            self.player3.add_card((2,2))












