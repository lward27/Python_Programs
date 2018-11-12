x = range(1,11)
for k in x:
		print k,
for k in []:
		print "foo"
# find 1 + 4 + 9 + 16 + ... + 10000

total = 0
for k in range(1,101):
		total += k**2
print total

##find factorail(100)

product = 1
for k in range(0,100):
		product *= k + 1
print product
print
x = ["aardvark", "platypus", "asp", "baboon"]
## find a list of all things beginning with a
def beginsWithA(x):
		return x[0] in "aA"
def findAllAs(list):
		out = [0]
		for k in list:
				if beginsWithA(k):
						out.append(k)
		return out
for k in findAllAs(x):
		print k,
