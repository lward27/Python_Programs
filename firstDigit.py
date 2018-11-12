#0prec:  x is an integer
#postc:  returns the first digit of x
def firstDigit(x):
		list0 = list(str(x))
		return int(list0[0])
print "firstDigit(234643) = ", firstDigit(234643), "expected: 2"
print "firstDigit(4) = ", firstDigit(4), "expected: 4"
print "firstDigit(9999999) = ", firstDigit(9999999), "expected: 9"
