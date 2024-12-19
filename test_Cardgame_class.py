from unittest import TestCase
from unittest import mock
from unittest.mock import patch
from Cardgame_class import CardGame
from Deckofcards_class import DeckOfCard


class TestCardGame(TestCase):

    def setUp(self):
        """Set up two game instances for testing"""
        self.game1 = CardGame("player1", "player2")    # Default initialization
        self.game2 = CardGame("player", "player",10 ,10)  # same name

    # -------- Test init -------
    def test_init_valid_player1_default_card_amount(self):
        """Test the initialization of player1 with default card amount"""
        self.assertEqual(26, len(self.game1.player1.cards_list))

    def test_init_valid_player2_default_card_amount(self):
        """Test the initialization of player2 with default card amount"""
        self.assertEqual(26, len(self.game1.player2.cards_list))

    def test_init_valid_player1_card_amount_edge_26(self):
        """Test that player1 cards amount is correctly initialized with edge amount: 26"""
        game = CardGame("a", "b", 26,26)
        self.assertEqual(26, game.player1.card_amount)

    def test_init_valid_player2_card_amount_edge_26(self):
        """Test that player2 cards amount is correctly initialized with edge amount: 26"""
        game = CardGame("a", "b", 26,26)
        self.assertEqual(26, game.player2.card_amount)

    def test_init_valid_player1_card_amount_edge_10(self):
        """Test that player1 cards amount is correctly initialized with edge amount: 10"""
        self.assertEqual(10, self.game2.player1.card_amount)

    def test_init_valid_player2_card_amount_edge_10(self):
        """Test that player2 cards amount is correctly initialized with edge amount: 10"""
        game = CardGame("a", "b", 10,10)
        self.assertEqual(10, self.game2.player2.card_amount)

    def test_init_valid_name_player1(self):
        """Test that player1's name is set correctly"""
        self.assertEqual("player1", self.game1.player1.player_name)

    def test_init_valid_name_player2(self):
        """Test that player2's name is set correctly"""
        self.assertEqual("player2", self.game1.player2.player_name)

    def test_init_valid_same_names(self):
        """Test that if both players have the same name, the second player's name is changed"""
        self.assertEqual("player2", self.game2.player2.player_name)

    def test_init_valid_same_names_player1(self):
        """Test that if both players have the same name, the first player's name stays the same"""
        self.assertEqual("player", self.game2.player1.player_name)

    def test_init_deck_of_cards_created(self):
        """Test that a DeckOfCard object is created during game initialization"""
        self.assertEqual(DeckOfCard,type(self.game1.deck_of_cards))

    def test_init_invalid_name1_type(self):
        """Test that a TypeError is raised when the first player name is not a string"""
        with self.assertRaises(TypeError):
            CardGame(1,"player")

    def test_init_invalid_name2_type(self):
        """Test that a TypeError is raised when the second player name is not a string"""
        with self.assertRaises(TypeError):
            CardGame("player",[])

    def test_init_invalid_card_amount1_type(self):
        """Test that a TypeError is raised when the first card amount is not an integer"""
        with self.assertRaises(TypeError):
            CardGame("player1","player2", "26", 26)

    def test_init_invalid_card_amount2_type(self):
        """Test that a TypeError is raised when the second card amount is not an integer"""
        with self.assertRaises(TypeError):
            CardGame("player1","player2", 10, [10])

    def test_init_card_amount1_small_9(self):
        """Test that if the first card amount is less than 10, it defaults to 26 cards"""
        game = CardGame("player1", "player2", 9, 26)
        self.assertEqual(26, game.player1.card_amount)

    def test_init_card_amount2_small_9(self):
        """Test that if the second card amount is less than 10, it defaults to 26 cards"""
        game = CardGame("player1", "player2", 26, 9)
        self.assertEqual(26, game.player2.card_amount)

    def test_init_card_amount1_big_27(self):
        """Test that if the first card amount is greater than 26, it defaults to 26 cards"""
        game = CardGame("player1", "player2", 27, 26)
        self.assertEqual(26, game.player1.card_amount)

    def test_init_card_amount2_big_27(self):
        """Test that if the second card amount is greater than 26, it defaults to 26 cards"""
        game = CardGame("player1", "player2", 26, 27)
        self.assertEqual(26, game.player2.card_amount)

    @mock.patch('Cardgame_class.CardGame.new_game')
    def test_init_new_game_activated(self, mock_new_game):
        """Test that the new_game method is called during the initialization of the game"""
        CardGame("player1", "player2")
        mock_new_game.assert_called_once()   # Ensure Mock is called once during initialization

    # -------- Test new game -------

    def test_new_game_valid_deck_empty(self):
        """Test that the game deck cards amount is empty after new_game initialization"""
        self.assertEqual(0, len(self.game1.deck_of_cards.cards_list))

    def test_new_game_valid_deck(self):
        """Test that the game deck cards amount is correct after new_game initialization"""
        self.assertEqual(32, len(self.game2.deck_of_cards.cards_list))

    def test_new_game_player1_hand(self):
        """Test that player1 hand has correct amount of cards"""
        self.assertEqual(26, len(self.game1.player1.cards_list))

    def test_new_game_player2_hand(self):
        """Test that player2 hand has correct amount of cards"""
        self.assertEqual(26, len(self.game1.player2.cards_list))

    def test_new_game_initialized_is_True_deck(self):
        """Test that calling new_game after initialization does nothing (deck stays the same)"""
        original_deck = self.game1.deck_of_cards.cards_list[:]
        self.game1.initialized = True
        self.game1.new_game()
        self.assertEqual(original_deck,self.game1.deck_of_cards.cards_list)

    def test_new_game_initialized_is_True_player1(self):
        """Test that calling new_game after initialization does nothing (player1 hand stays the same)"""
        original_hand = self.game1.player1.cards_list[:]
        self.game1.initialized = True
        self.game1.new_game()
        self.assertEqual(original_hand,self.game1.player1.cards_list)

    def test_new_game_initialized_is_True_player2(self):
        """Test that calling new_game after initialization does nothing (player2 hand stays the same)"""
        original_hand = self.game1.player2.cards_list[:]
        self.game1.initialized = True
        self.game1.new_game()
        self.assertEqual(original_hand,self.game1.player2.cards_list)

    @mock.patch('Cardgame_class.DeckOfCard.card_shuffle')
    def test_new_game_shuffle_is_activated(self, mock_shuffle):
        """Test that the deck is shuffled once during the new_game process"""
        game = CardGame("a", "b")
        mock_shuffle.assert_called_once()    # Ensure Mock is called once

    @mock.patch('Player_class.Player.set_hand')
    def test_new_game_set_hand_active_twice(self, mock_set_hand):
        """Test that the set_hand method is called exactly twice during new_game"""
        game = CardGame("a", "b")
        self.assertEqual(mock_set_hand.call_count, 2)   # Ensure Mock was called twice

    # ------ Test get winner --------

    def test_get_winner_valid_player1(self):
        """Test that the correct winner is identified when player1 has more cards"""
        game = CardGame("a", "b", 20, 10)
        self.assertEqual(game.player1, game.get_winner())

    def test_get_winner_valid_player2(self):
        """Test that the correct winner is identified when player2 has more cards"""
        game = CardGame("a", "b", 20, 26)
        self.assertEqual(game.player2, game.get_winner())

    def test_get_winner_valid_None(self):
        """Test that get_winner returns None when both players have the same card amount."""
        self.assertEqual(None, self.game1.get_winner())






