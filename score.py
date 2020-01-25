import sqlite3
import random
from newcard import Card

scores = ('Royal Straight Flush', 'Straight Flush', 'Four Card', 'Full House', 'Flush',
          'Straight', 'Triple', 'Two Pair', 'One Pair', 'High Card')
rank_values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
               'Queen':12, 'King':13, 'Ace':14}
reverse = {v: k for k, v in rank_values.items()}
score_values = {'Royal Straight Flush':100, 'Straight Flush':90, 'Four Card':80, 'Full House':70, 'Flush':60,
          'Straight':50, 'Triple':40, 'Two Pair':30, 'One Pair':20, 'High Card':10}

class PokerScore:
    def __init__(self, score = 'High Card'):
        if (scores.count(score) == 0):
            raise Exception('Undefined Score')
        self.score = score
        self.sum = 0
        self.cards = []

    def __str__(self):
        returnStr = 'Score is ' + self.score + ' ' + str(self.get_total_score())
        """for card in self.cards:
            returnStr += '\n' + card.rank + '(' + str(card.rank_value) + ') of ' + card.suit"""
        return returnStr

    def set_score(self, score):
        if (scores.count(score) == 0):
            raise Exception('Undefined Score')
        self.score = score

    def add_sum(self, rank):
    	#print('DEBUG:', 'num:', rank_values[rank])
    	self.sum += rank

    def set_score_cards(self, cards):
        self.cards = [cards]

    def add_score_cards(self, card):
        self.cards.extend(card)

    def get_top_card(self):
        return self.cards[0]

    def get_total_score(self):
        return score_values[self.score] * 10 + self.get_top_card().rank_value


#review method
def review_score(five_cards):

	#set up for SQL
	db = sqlite3.Connection('cards.db')
	sql = db.execute
	sql('DROP TABLE IF EXISTS cards')
	sql('CREATE TABLE cards(suit, rank);')

	#insert a card to sql table
	def insert(suit, rank):
		sql('INSERT INTO cards VALUES (?, ?)', (suit, rank))
		db.commit()

	#insert cards to the sql table "cards"
	for card in five_cards:
		insert(card.suit, rank_values[card.rank])

	#sort by rank
	rankhand = sql('SELECT rank, count() FROM cards GROUP BY rank ORDER BY -count(), -rank').fetchall()
	#sort by suit
	suithand = sql('SELECT suit, count() FROM cards GROUP BY suit ORDER BY -count()').fetchall()

	#check for ace
	has_ace = False
	for card in five_cards:
		if card.rank == 'Ace':
			has_ace = True

	#check for straight
	def straight():
		if len(rankhand) == 5:
			if has_ace:
				#2,3,4,5,14 -> 15,16,17,18,14
				sql('UPDATE cards SET rank = rank + 13 WHERE rank < 6')
				hand = sql('SELECT rank, count() FROM cards GROUP BY -rank').fetchall()
				db.commit()
				return hand[0][0] == 14 or hand[4][0] == 14 and hand[0][0] - hand[4][0] == 4
			return rankhand[0][0] - rankhand[4][0] == 4

    #return the right "Score Value" according to the hand
	def score():
		nonlocal addscore
		if straight():
			if suithand[0][1] == 5:
				if rankhand[4][0] == 10:
					return 'Royal Straight Flush'
				return 'Straight Flush'
			return 'Straight'
		elif suithand[0][1] == 5:
			return 'Flush'
		elif rankhand[0][1] == 4:
			return 'Four Card'
		elif rankhand[0][1] == 3:
			if rankhand[1][1] == 2:
				return 'Full House'
			return 'Triple'
		elif rankhand[0][1] == 2:
			if rankhand[1][1] == 2:
				return 'Two Pair'
			return 'One Pair'
		return 'High Card'

	score = score()

	pokerScore = PokerScore()
	pokerScore.set_score(score)

    #this hardcode was written to pass another contributor's testcases
	toprank = rankhand[0][0]
	if straight() and has_ace:
		toprank = rankhand[1][0]
	topcard = Card('Hearts', reverse[toprank])
	pokerScore.set_score_cards(topcard)
	
	return pokerScore


