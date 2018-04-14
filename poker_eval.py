"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; 
for example, a pair of eights beats a pair of fives (see example 1 below). 
But if two ranks tie, for example, both players have a pair of queens, then highest cards 
in each hand are compared (see example 4 below); if the highest cards tie then the next 
highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): 
the first five are Player 1's cards and the last five are Player 2's cards. 
You can assume that all hands are valid (no invalid characters or repeated cards), 
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?

curl https://projecteuler.net/project/resources/p054_poker.txt > poker.txt


https://projecteuler.net/problem=54


"""


ex_hands = ['8C TS KC 9H 4S', '7D 2S 5D 3S AC', '5C AD 5D AC 9C' ,
			'7C 5H 8D TD KS', '3H 7H 6S KC JS' ,'QH TD JC 2D 8S' ,
			'QD AS 6H JS 2C' , '3D 9H KC 4H 8S', 'KD 8S 9S 7C 2S' ,
			'3S 6D 6S 4H KC']

class PokerHand():
	def __init__(self, card_string):
		self.face_dict = {'2' : 2 , '3' : 3, '4' : 4, '5' : 5, 
			'6' :  6, '7': 7, '8' : 8, '9' : 9, 
			'T' : 10, 'J': 11, 'Q': 12 ,'K' : 13, 'A' : 14}

		self.suit_dict = {'C' : 1, 'H' : 2, 'S' : 3, 'D' : 4}


		self.cards = [ (self.face_dict[x[0]], 
							self.suit_dict[x[1]] ) 
							for x in card_string.split()]

		#the face values, for rank comparison
		self.face_vals = sorted([x[0] for x in self.cards])[::-1]

		#the count of each card, 
		self.val_count = { k:0 for k in self.face_dict.values()}
		#the count of suit comparisons, for flush checking
		self.suit_count = { k:0  for k in self.suit_dict.values()}
		
		for x in self.cards:
			self.val_count[x[0]] += 1
			self.suit_count[x[1]] += 1

		self.score_hand()

	def is_straight(self):
		if self.face_vals[4] ==  (self.face_vals[0] - 4):
			self.straight = 1
		else:
			self.straight = 0

	def is_flush(self):
		self.flush = 0
		for x in self.suit_count.values():
			if x == 5:
				self.flush = 1

	def is_multiples(self):
		self.quad = 0
		self.triple = 0
		self.doubles = []
		for k,v in self.val_count.items():
			if v == 4:
				self.quad = k
			if v == 3:
				self.triple = k
			if v == 2:
				self.doubles.append(k)
		self.doubles = 	sorted(self.doubles)[::-1]


	def score_hand(self):
		self.is_straight()
		self.is_flush()
		self.is_multiples()

	@property
	def components(self):
		# (flush(bool), straight(bool), quad(suit_#), triple(suit_#), double(tuple of suit #s), card_rank_tuple)

		return  (self.flush, 
					self.straight,
					self.quad,
					self.triple,
					self.doubles,
					self.face_vals)

filename='poker.txt'

def game(filename):
	p1_wins = 0
	p2_wins = 0

	with open(filename) as file:
		for line in file:
			dat = line.rstrip()
			p1 = PokerHand(dat[:14])
			p2 = PokerHand(dat[15:])


x = PokerHand('8C TS KC 9H 4S')
x.cards
x.components












