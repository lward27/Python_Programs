#ask user his age
#if the user is under 21, tell him to "Skeedaddle, Punk!"
#otherweise tell hime "NAME YER POISON
def threewayFork(age):
		if age >= 65:
				print "shall i cash yer social, geezar??"
		elif age < 21:
				print "SKEDADDLE, PUNK!"
		else:
				print "Name yer poison.."

age = input("enter your age:   ")
threewayFork(age)
