## blackjack, war, poker

import random
import sys
from Card import *
from Hand import *
from Shoe import *

print "Welcome to the best gaming experience of your natural born life..."


## games

def war():
	print "war"

def poker():
	print "poker"

def blackjack():
	deck = Shoe()
	hand = deck.deal(2)
	print "you were dealt", hand[0], "and", hand[1]
	hitorquit = raw_input("hit? (y/n)  ")
	k = 2
	while hitorquit is "y":
		if hitorquit is "y":
			hand = hand + deck.deal(1)
			print "you now have a", hand[k]
			hitorquit = raw_input("hit? (y/n)  ")
			k += 1
	if hitorquit is "n":
			f = random.randint(18,21)
			total = input("enter your total!"  )
			if total < 21 and total > f:
				print "YOU WIN!!"
				x = 1
			elif total < f:
				print "YOU LOSE!!"
			elif total == f:
				print "A TIE!! DEALER WINS.. WHO EVER THAT IS!"
			elif total > 21:
				print "FOLDED!!"
			print "the computer was dealt", f
			entrance = raw_input("play again? (y/n)  ")
			while entrance is "y":
				if entrance is "y":
					return play(enter) 
				elif entrance is "n":
					return sys.exit(0)
## introduction
def play(enter):
	if enter is "a":
		return blackjack()
	elif enter is "b":
		return war()
	elif enter is "c":
		return poker()
enter = raw_input("would you like to play \n (a) blackjack \n (b) war \n (c) poker \nenter(a/b/c):  ")
play(enter)
