import random
import sys #check out argv, it's way cool
## 1 if head, 0 if tails
def toss():
	return random.randint(0,1)
def tossTen():
	total = 0
	for k in range(10):
		total += toss()
	return total
tally = [0]*11
#for k in xrange(1000000):
k = 0
while k < 1024000:
	tally[tossTen()] += 1
	k += 1
print tally
