from unittest import TestCase
from Card_class import Card

class TestCard(TestCase):

    def setUp(self):
        """Set up two cards for testing"""
        self.card1 = Card(2,1)
        self.card2 = Card(14,4)


    #----- Test init ------

    def test_init_valid_value_low_edge_2(self):
        """Test the initialization of a card with edge value: 2"""
        self.assertEqual(2, self.card1.value)

    def test_init_valid_value_upper_edge_14(self):
        """Test the initialization of a card with edge value: 14"""
        self.assertEqual(14, self.card2.value)

    def test_init_valid_suit_low_edge_1(self):
        """Test the initialization of a card with suit edge value: 1"""
        self.assertEqual(1, self.card1.suit)

    def test_init_valid_suit_upper_edge_4(self):
        """Test the initialization of a card with suit edge value: 4"""
        self.assertEqual(4, self.card2.suit)

    def test_init_invalid_value_type(self):
        """Test that a TypeError is raised when value type is incorrect"""
        with self.assertRaises(TypeError):
            Card("235210", 2)

    def test_init_invalid_suit_type(self):
        """Test that a TypeError is raised when suit type is incorrect"""
        with self.assertRaises(TypeError):
            Card(4, [])

    def test_init_invalid_value_low_1(self):
        """Test that a TypeError is raised when value is out of range: 1"""
        with self.assertRaises(ValueError):
            Card(1,3)

    def test_init_invalid_value_upper_15(self):
        """Test that a TypeError is raised when value is out of range: 15"""
        with self.assertRaises(ValueError):
            Card(15,3)

    def test_init_invalid_suit_low_0(self):
        """Test that a TypeError is raised when suit value is out of range: 0"""
        with self.assertRaises(ValueError):
            Card(6,0)

    def test_init_invalid_suit_upper_5(self):
        """Test that a TypeError is raised when suit value is out of range: 5"""
        with self.assertRaises(ValueError):
            Card(12,5)

    # ----- Test gt ------

    def test_gt_valid_value_is_different_True(self):
        """Test that a card with a higher value is considered greater"""
        self.assertTrue(self.card2 > self.card1)

    def test_gt_valid_different_suit_True(self):
        """Test that a card with the same value but a higher suit is considered greater"""
        card3 = Card(2,2)
        self.assertTrue(card3 > self.card1)

    def test_gt_valid_different_value_False(self):
        """Test that a card with a lower value is not considered greater"""
        self.assertFalse(self.card2 < self.card1)

    def test_gt_valid_different_suit_False(self):
        """Test that a card with the same value but a lower suit is not considered greater"""
        card3 = Card(2,2)
        self.assertFalse(card3 < self.card1)

    def test_gt_equal_cards_False(self):
        """Test that two identical cards are not considered greater than each other"""
        card3 = Card(2, 1)
        self.assertFalse(card3 < self.card1)

    def test_gt_invalid_other_type(self):
        """Test that a TypeError is raised when other is not a Card"""
        with self.assertRaises(TypeError):
            print(self.card2 > 3)

    # ---- Test eq -----
    def test_eq_valid_True(self):
        """Test that two cards with the same value and suit are considered equal"""
        card3 = Card(2,1)
        self.assertTrue(self.card1 == card3)

    def test_eq_valid_False_different_value(self):
        """Test that two cards with different values are not considered equal"""
        card3 = Card(3,1)
        self.assertFalse(self.card1 == card3)

    def test_eq_valid_False_different_suit(self):
        """Test that two cards with the same value but different suits are not considered equal"""
        card3 = Card(2,2)
        self.assertFalse(self.card1 == card3)

    def test_eq_invalid_other_type(self):
        """Test that a TypeError is raised when other is not a Card"""
        with self.assertRaises(TypeError):
            print(self.card1 == [])

