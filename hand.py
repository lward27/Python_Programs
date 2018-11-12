from Card import *
from Shoe import *
class Hand:
	def __init__(self):
		self.cards = []
	def __str__(self):
		out = ""
		for k in self.cards:
			out += str(k) + "\n"
		return out
	def __getitem__(self, index):
		return self.cards[index]
	def take(self, newCards):
		self.cards += newCards
	def sort(self):
		self.cards.sort() 
		#self.cards.reverse()
