import sys
def median(x):
	type(x) == type([])
	x.sort()
	if (len(x)) % 2 != 0:
		k = (len(x)/2)
		return x[k]
	else:
		k = (len(x)/2)
		return x[k], x[k-1]


def keepLonger(tooSmall, list1):
	type(list1) == type([])
	x = []
	for k in list1:
		if len(k) > tooSmall:
			x.append(k)
	return x
		
import math
def figgie(x):
	sqrt1 = 0
	k = x/2
	while k - math.sqrt(x) > (1*10**-10):
		sqrt1 = k
		k = (.5*(k + (x/k)))
	return sqrt1

print "median([1,3,2,4,5]) = ", median([1,3,2,4,5]), "expected: 3"
print "median([1,5,2,3,6,7]) = ", median([1,5,2,3,6,7]), "expected: 5,3"
print "keepLonger(2, ['h', 'hi', 'hey', 'help', 'hello']) = ", keepLonger(2, ["h", "hi", "hey", "help", "hello"]), "expected: ['hey', 'help', 'hello']"
print "keepLonger(3, ['h', 'hippolite', 'hey', 'help', 'word']) =", keepLonger(3, ["h", "hippolite", "hey", "help", "word"]), "expected: ['hippolite', 'help', 'word']"
print "figgie(36) = ", figgie(36), "expected: 6"
print "figgie(100) = ", figgie(100), "expected: 10"
