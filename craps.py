import random
def rollDice():
		return random.randint(1,6) + random.randint(1,6)
firstRoll = rollDice()
print "you rolled a ", firstRoll, "on your first roll."
if firstRoll in [2,3,12]:
		print "Craps!  A LOSER!"
elif firstRoll in [7,11]:
		print "Natural.... a winner!!"
else:
		point = firstRoll
		print "your point is", point 
		currentRoll = rollDice()
		while currentRoll != point and currentRoll != 7:
				print "You rolled", currentRoll
				currentRoll = rollDice()
		if currentRoll == 7:
				print "house beat your point since you rolled 7. you LOSE"
		elif currentRoll == point:
				print "You won the hard way by rolling", point
