#prec:  moe, larry, joe are integers
#post:  returns true if moe < larry <= joe.
def isIncreasing(moe, larry, joe):
		if moe < larry <= joe:
				print "true"
		else: print "false"
print "isIncreasing(1, 2, 3) = ",
isIncreasing(1, 2, 3)
print "expected: true" 
print "isIncreasing(4, 2, 3) = ",
isIncreasing(4, 2, 3) 
print "expected: false"
