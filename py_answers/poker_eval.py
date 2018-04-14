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
		self.face_dats = sorted([x[0] for x in self.cards])[::-1]

		#the count of each card, 
		self.val_count = { k:0 for k in self.face_dict.values()}
		#the count of suit comparisons, for flush checking
		self.suit_count = { k:0  for k in self.suit_dict.values()}
		
		for x in self.cards:
			self.val_count[x[0]] += 1
			self.suit_count[x[1]] += 1

		self.score_hand()

	def is_straight(self):		
		if self.face_dats[4] == (self.face_dats[0] - 4) and len(set(self.face_dats)) == 5:
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
		for k, v in self.val_count.items():
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
					self.face_dats)


def high_card(p1_dat, p2_dat):
	print(p1_dat, p2_dat)
	""" determine winner based on who has the higher card"""
	while len(p1_dat) > 0 and len(p2_dat) > 0:
		if p1_dat[0] == p2_dat[0]:
			p1_dat.pop(0)
			p2_dat.pop(0)
		elif p1_dat[0] > p2_dat[0]:
			return (1,0)
		elif p1_dat[0] < p2_dat[0]:
			return (0,1)
	return(0,0)

def compare_hands(p1, p2):
	""" take in two PokerHand class instances and determine the winner
		output (1,0) is p1 wins and (0,1) if p2 wins """
	p1_win = (1,0)
	p2_win = (0,1)
	p1_dat = p1.components
	p2_dat = p2.components

	# two straight flushes, 
	if p1_dat[0] == 1 and p1_dat[1] == 1 and p2_dat[0] == 1 and p2_dat[1] == 1 :
		return high_card(p1_dat[-1], p2_dat[-1])

	elif  p1_dat[0] == 1 and p1_dat[1] == 1 :
		return p1_win

	elif p2_dat[0] == 1 and p2_dat[1] == 1 :
		return p2_win

	#check for quads
	elif p1_dat[2] != 0 and p2_dat[2] != 1 :
		return high_card(p1_dat[-1], p2_dat[-1])

	elif p1_dat[2] != 0 :
		return p1_win

	elif p2_dat[2] != 0 :
		return p2_win

	#full house
	elif p1_dat[3] != 0 and len(p1_dat[4]) != 0 and p2_dat[3] != 0 and len(p2_dat[4]) != 0 :
		#cant have matching triples on double full house, so only check triples
		if p1_dat[3] > p2_dat[3]:
			return p1_win
		elif p1_dat[3] < p2_dat[3]:
			return p2_win
	
	elif p1_dat[3] != 0 and len(p1_dat[4]) != 0 :
		return p1_win

	elif p2_dat[3] != 0 and len(p2_dat[4]) != 0 :
		return p2_win

	#flush
	elif p1_dat[0] == 1  and p2_dat[0] == 1  :
		return high_card(p1_dat[-1], p2_dat[-1])

	elif p1_dat[0] == 1 :
		return p1_win

	elif p2_dat[0] == 1 :
		return p2_win

	#straight
	elif p1_dat[1] == 1 and p2_dat[1] == 1 :
		return high_card(p1_dat[-1], p2_dat[-1])

	elif p1_dat[1] == 1 :
		return p1_win

	elif p2_dat[1] == 1 :
		return p2_win

	#3 of a kind

	elif p1_dat[3] > p2_dat[3]:
		return p1_win
	elif p1_dat[3] < p2_dat[3]:
			return p2_win
	
	#two pairs
	elif len(p1_dat[4]) > 1 and len(p2_dat[4]) > 1:
		if p1_dat[4][0] == p2_dat[4][0]:
			if p1_dat[4][1] == p2_dat[4][1]:
				return high_card(p1_dat[-1], p2_dat[-1])
			
			elif p1_dat[4][1] > p2_dat[4][1]:
				return p1_win
			
			elif p1_dat[4][1] < p2_dat[4][1]:
				return p2_win

		elif p1_dat[4][0] > p2_dat[4][0]:
			return p1_win
		
		elif p1_dat[4][0] < p2_dat[4][0]:
			return p2_win
	
	elif len(p1_dat[4]) > 1:
			return p1_win

	elif len(p2_dat[4]) > 1:
			return p2_win

	#pairs
	elif len(p1_dat[4]) == 1 and len(p2_dat[4]) == 1:
		if p1_dat[4][0] == p2_dat[4][0]:
			return high_card(p1_dat[-1], p2_dat[-1])

		elif p1_dat[4][0] > p2_dat[4][0]:
			return p1_win
		
		elif p1_dat[4][0] < p2_dat[4][0]:
			return p2_win
	
	elif len(p1_dat[4]) == 1:
		return p1_win

	elif len(p2_dat[4]) == 1:
		return p2_win

	#high card
	else:
		return high_card(p1_dat[-1], p2_dat[-1])

def poker_game(filename):
	p1_wins = 0
	p2_wins = 0

	with open(filename) as file:
		for i, line in enumerate(file):

			dat = line.rstrip()
			p1 = PokerHand(dat[:14])
			p2 = PokerHand(dat[15:])
			print(i)
			print(p1.components, p2.components)

			winner = compare_hands(p1, p2)
			p1_wins += winner[0]
			p2_wins += winner[1]

	return f"player 1 wins: {p1_wins}, player 2 wins: {p2_wins}.\n"



filename='poker.txt'


poker_game(filename)




"""
Below is for testing:

take a set of hands and a set of of matchups and 
make sure that the components are properly identified and that the winners are
properly identified

"""


straight_flush = 'AC KC QC JC TC'
sf = PokerHand(straight_flush)
sf.components

straight = 'TC 7H 6H 9D 8S '
s = PokerHand(straight)
s.components

flush = '2C 9C QC 7C TC'
f = PokerHand(flush)
f.components

full_house = '9C 7C 9H 7S 9S'
fh = PokerHand(full_house)
fh.components

quad = '5C 5H 5S 5D 9S'
q = PokerHand(quad)
q.components

triple = '7H 9H 7C 2H 7D'
t = PokerHand(triple)
t.components

two_pairs = '7H 9H 7C 2H 2D'
tp = PokerHand(two_pairs)
tp.components

pair = '6H 9H 6C 3H 2D'
p = PokerHand(pair)
p.components

nil = 'KH 9H 6C 3H 2D'
n = PokerHand(nil)
n.components

#nil is beating pairs!


hands = [ sf, s, f, fh, q, t, tp, p, n]

for h1 in hands:
	for h2 in hands:
		if h1.components == h2.components:
			continue

		compare = compare_hands(h1, h2)
		print(f'winner:{compare}\nh1:{h1.components}\th2:{h2.components}')
