#prec:  x is a number
#postc:  returns the fractional part of the number
#example:  fracPart(4.5) = .5,  fracPart(-3.1) = .9
def fracPart(x):
		return 1 - (x%1)

print "fracPart(5.5) = ", fracPart(5.5), "expected: .5"
print "fracPart(56.78) = ", fracPart(56.78), "expected: .22"
print "fracPart(-12.2) = ", fracPart(-12.2), "expected: .2"
		
