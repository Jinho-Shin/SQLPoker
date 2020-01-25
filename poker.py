from newcard import Card, Deck
from newscore import PokerScore, review_score
from itertools import combinations

class PokerPlayer:

    def __init__(self, name = ''):
        self.name = name
        self.seven_cards = []
        self.PokerScores = []

    def __str__(self):
        returnStr = 'Player is ' + self.name + ' '
        for card in self.seven_cards:
            returnStr += '\n' + card.rank + '(' + str(card.rank_value) + ') of ' + card.suit
        return returnStr

    def add_card(self, card):
        self.seven_cards.append(card)
        if (len(self.seven_cards) > 7):
            raise Exception('No more than seven cards')

    def review_all_fiver_hands(self):
        if (len(self.seven_cards) != 7):
            raise Exception('Need seven cards')

        # review all the 5 cards combinations from given 7 cards
        scores = []
        for comb_cards in list(combinations(self.seven_cards, 5)):
            pokerScore = review_score(comb_cards)
            scores.append(pokerScore)

        # return sorted score
        self.PokerScores = sorted(scores, key=lambda x: x.get_total_score(), reverse=True)
        return self.PokerScores

    def get_top_poker_score(self):
        return self.PokerScores[0]


class PokerGame:

    def play(self):
        poker_players = []

        num_players = input("How many players? ")
        for i in range(int(num_players)):
            player_name = input("Name of poker player {}? ".format(i+1))
            poker_player = PokerPlayer(player_name)
            poker_players.append(poker_player)

        print("Dealing cards")
        deck = Deck()
        deck.shuffle()
        for i in range(7):
            for poker_player in poker_players:
                poker_player.add_card(deck.deal())
                print(poker_player)

            if (i < 6):
                dealmore = input("Deal more card(y or n)? ")
                if (dealmore.lower() == 'n'):
                    return

        for poker_player in poker_players:
            poker_player.review_all_fiver_hands()
            poker_score = poker_player.get_top_poker_score()
            print(poker_player.name.center(30,'-'))
            print(poker_score)

if __name__ == '__main__':
    poker_game = PokerGame()
    poker_game.play()
