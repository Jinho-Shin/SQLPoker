import unittest
from newcard import Card, Deck
from newscore import review_score
from newkpoker import PokerPlayer

class PokerScoreTestCase(unittest.TestCase):

    def test_ace_straight_true(self):
        cards = []
        cards.append(Card('Hearts', 'Ace'))
        cards.append(Card('Spades', 'Two'))
        cards.append(Card('Hearts', 'Three'))
        cards.append(Card('Hearts', 'Four'))
        cards.append(Card('Clubs', 'Five'))

        pokerScore = review_score(cards)

        self.assertEqual(pokerScore.score == 'Straight', True)
        # Ace should be low instead of high
        self.assertEqual(pokerScore.get_top_card().rank == 'Five', True)

    def test_ace_straight_false(self):
        cards = []
        cards.append(Card('Hearts', 'Ace'))
        cards.append(Card('Spades', 'Two'))
        cards.append(Card('Hearts', 'Two'))
        cards.append(Card('Hearts', 'Four'))
        cards.append(Card('Clubs', 'Five'))

        pokerScore = review_score(cards)

        self.assertEqual(pokerScore.score == 'Straight', False)

    def test_royal_straight_flush_true(self):
        cards = []
        cards.append(Card('Spades', 'Ten'))
        cards.append(Card('Spades', 'Jack'))
        cards.append(Card('Spades', 'Queen'))
        cards.append(Card('Spades', 'King'))
        cards.append(Card('Spades', 'Ace'))

        pokerScore = review_score(cards)

        self.assertEqual(pokerScore.score == 'Royal Straight Flush', True)

    def test_straight_true(self):
        cards = []
        cards.append(Card('Spades', 'Ten'))
        cards.append(Card('Hearts', 'Jack'))
        cards.append(Card('Diamonds', 'Queen'))
        cards.append(Card('Spades', 'King'))
        cards.append(Card('Spades', 'Nine'))

        pokerScore = review_score(cards)

        self.assertEqual(pokerScore.score == 'Straight', True)
        self.assertEqual(pokerScore.get_top_card().rank == 'King', True)

    def test_four_card_true(self):
        cards = []
        cards.append(Card('Spades', 'Ten'))
        cards.append(Card('Hearts', 'Ten'))
        cards.append(Card('Clubs', 'Ten'))
        cards.append(Card('Spades', 'Ten'))
        cards.append(Card('Spades', 'Ace'))

        pokerScore = review_score(cards)

        self.assertEqual(pokerScore.score == 'Four Card', True)
        self.assertEqual(pokerScore.get_top_card().rank == 'Ten', True)

    def test_two_pair_true(self):
        cards = []
        cards.append(Card('Spades', 'Ten'))
        cards.append(Card('Hearts', 'Ten'))
        cards.append(Card('Clubs', 'Two'))
        cards.append(Card('Spades', 'Two'))
        cards.append(Card('Spades', 'Ace'))

        pokerScore = review_score(cards)

        self.assertEqual(pokerScore.score == 'Two Pair', True)
        self.assertEqual(pokerScore.get_top_card().rank == 'Ten', True)

    def test_full_house_true(self):
        cards = []
        cards.append(Card('Spades', 'Two'))
        cards.append(Card('Hearts', 'Ten'))
        cards.append(Card('Clubs', 'Two'))
        cards.append(Card('Diamonds', 'Two'))
        cards.append(Card('Spades', 'Ten'))

        pokerScore = review_score(cards)

        self.assertEqual(pokerScore.score == 'Full House', True)
        self.assertEqual(pokerScore.get_top_card().rank == 'Two', True)

    def test_poker_player_one_pair(self):
        pokerPlayer = PokerPlayer()

        pokerPlayer.add_card(Card('Spades', 'Two'))
        pokerPlayer.add_card(Card('Hearts', 'Ten'))
        pokerPlayer.add_card(Card('Clubs', 'Three'))
        pokerPlayer.add_card(Card('Diamonds', 'Two'))
        pokerPlayer.add_card(Card('Spades', 'Nine'))
        pokerPlayer.add_card(Card('Diamonds', 'Queen'))
        pokerPlayer.add_card(Card('Spades', 'King'))

        pokerScores = pokerPlayer.review_all_fiver_hands()

        # index 0 is the top score
        self.assertEqual(pokerScores[0].score == 'One Pair', True)
        self.assertEqual(pokerScores[0].get_top_card().rank == 'Two', True)

    def test_poker_player_full_house(self):
        pokerPlayer = PokerPlayer()

        pokerPlayer.add_card(Card('Spades', 'Two'))
        pokerPlayer.add_card(Card('Hearts', 'Ten'))
        pokerPlayer.add_card(Card('Clubs', 'Two'))
        pokerPlayer.add_card(Card('Diamonds', 'Two'))
        pokerPlayer.add_card(Card('Spades', 'Ten'))
        pokerPlayer.add_card(Card('Diamonds', 'Nine'))
        pokerPlayer.add_card(Card('Spades', 'King'))

        pokerScores = pokerPlayer.review_all_fiver_hands()

        self.assertEqual(pokerScores[0].score == 'Full House', True)
        self.assertEqual(pokerScores[0].get_top_card().rank == 'Two', True)


if __name__ == '__main__':
    unittest.main()
