##This is a general purpose system for a standard deck of 52 playing
##cards.
import random
#class to represent individual playing cards
class Card:
	def __init__(self, number = -1):
		random.seed()
		if number == -1:
			self.number = random.randint(0,52)
		else:
			self.number = number
		self.ranks = [u'2','3','4','5','6','7','8','9','10','J','Q','K','A']
		self.suits = ['clubs', 'diamonds', 'hearts', 'spades']
	def __str__(self):
		return self.ranks[self.number%13]+ " of " + self.suits[self.number/13]
	def rank(self):
		return self.ranks[self.number%13]
	def numericalRank(self):
		return 2 + self.ranks.index(self.rank())
	def compareRankTo(self, other):
		return self.numericalRank() - other.numericalRank()
	def showNumber(self):
		return self.number
	def __cmp__(self, other):
		return self.number - other.number
	def suit(self):
		return self.suits[self.number%4]
	def __eq__(self, other):
		return self.number == other.number
