#class to represent a shoe of playing cards and manage deals from it.
#this class depends on the class Card
import random
from Card import *
class Shoe:
	def __init__(self, n = 1):
		random.seed
		self.cards = [Card(k%52) for k in range(0,52*n)]   #put cards in and shuffle
		random.shuffle(self.cards)
	def deal(self, n = 1):#number of cards to be dealt
		tmp = self.cards[0:n]  #store cards
		self.cards[0:n] = []   ##remove cards from the deck
		return tmp
	def showShoe(self):	
		for k in self.cards:
			print k
	def empty(self):
		return len(self.cards) > 0
	def cardsLeft(self):
		return len(self.cards)
	def shoeSize(self):   ##V2
		return 52*n
