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
print "median([1,3,2,4,5]) = ", median([1,3,2,4,5]), "expected: 3"
print "median([1,5,2,3,6,7]) = ", median([1,5,2,3,6,7]), "expected: 5,3"

