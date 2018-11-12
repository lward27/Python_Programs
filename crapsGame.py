	###   #####	   ##      #####    ####
      ##   #  ##   #	  ## #     ##   #  ##
      #	      #####	 ######    #####    ###
      ##   #  ##   #    ##     #   ##         ##
      	###   ##    #  ##       #  ##      ####

      #############################################
		       			  ###
			              ###
			          ###
				################

##########################################################
##							##	 
##greet the user					##
## offer to tell the rules, yes or no			##
## ask the user his stake (integer number of dollars)	##
##							##
## game is house, player is the player.			##	
##							##
## Run the rounds:					##
## get a bet. make sure it's legit.			##
## Tart reply for cheaters, and then resolicit bet	##
##	until it's legit				##
## Play							##
## Ask if the user wants to play again.			##
##							##
## When the user is done, tell him his final stake	##
##	and how much he won or lost			##
## guptaa@ncssm.edu							##
##########################################################
import random
import sys
print "Welcome to craps!"

def play(enter):
	if enter is "y":
		return
	elif enter is "n":
		return sys.exit(0)
	else:
		print "you entered ", enter, ", this is invalid command"
		return sys.exit(0)
enter = raw_input("would you like to play? (y/n)")
play(enter)

def rules(tell):
	if tell is "y":
		return
	elif tell is "n":
		print "rules"
	else:
		print "you entered ", tell, ", this is invalid command"
		return sys.exit(0)
tell = raw_input("Know how to play?? (y/n)")
rules(tell)

def rollDice():
	return random.randint(1,6) + random.randint(1,6)

def turn():
	firstRoll = rollDice()
	print "you rolled a ", firstRoll, "on your first roll."
	if firstRoll in [2,3,12]:
		print "Craps!  A LOSER!"
		return -1
	elif firstRoll in [7,11]:
		print "Natural.... a winner!!"
		return +1
	else:
		point = firstRoll
		print "your point is", point 
		currentRoll = rollDice()
		while currentRoll != point and currentRoll != 7:
			print "You rolled", currentRoll
			currentRoll = rollDice()
		if currentRoll == 7:
			print "house beat your point since you rolled 7. you LOSE"
			return -1
		elif currentRoll == point:
			print "You won the hard way by rolling", point
			return  +1
print turn(),
print
def keepplaying(dood):
	dood = raw_input("you really want keep playing this horrible game..? (y/n)")
	if dood is "y":
		return turn(), keepplaying(dood)
	elif dood is "n":
		return sys.exit(0)
dood = raw_input("keep playing (y/n)")
keepplaying(dood)
