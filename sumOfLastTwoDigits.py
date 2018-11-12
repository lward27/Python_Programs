#prec:  x is a nonnegative integer
#postc:  returns the sum of the last two digits of x
def sumOfLastTwoDigits(x):
		if x < 10:
				return "must be greater then ten!"
		list0 = list(str(x % 100))
		return int(list0[0]) + int(list0[1])
print "sumOfLastTwoDgits(456) = ", sumOfLastTwoDigits(456), "expected: 11"
print "sumOfLastTwoDgits(1000000098) = ", sumOfLastTwoDigits(1000000098), "expected: 17"
print "sumOfLastTwoDgits(5) = ", sumOfLastTwoDigits(5), "expected: look left, read."
