#precondition:   x is is an integer
#postcondition:  returns True if x is even and False otherwsie
def isEven(x):
	return (x%2) == 0
print "isEven(34) = ", isEven(34), "expected:  true"
print "isEven(3) = ", isEven(33), "expected: false"
print "isEven(1467) = ", isEven(31), "expected: false"
