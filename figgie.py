import math
def figgie(x):
	sqrt1 = 0
	k = x/2
	while k - math.sqrt(x) > (1*10**-10):
		sqrt1 = k
		k = (.5*(k + (x/k)))
	return sqrt1
print figgie(36)
