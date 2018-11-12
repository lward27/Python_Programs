import math
#Lucas Ward
#ProblemSet 3
#wardlPS3.py
def isnotList (x):
	return type(x) != type([])
def extractAtoms(x):
	#precondition: x a (possibly nested) list
	#postcondition:  return a list of all the atoms (non-list items)
	# in x.
	tally = []
	k = 0
	for k in range(0, int(len(x))):
		if isnotList(x[k]) == True:
			tally.append(x[k])
	return tally
def isPrime(x):
	#precondition: x is a positive integer
	#postcondition:  return True if x is prime and False otherwise
	#NB:  1 is NOT prime
	if x == 1:
		return False
	for k in range (2, int(x**0.5)+1):
		if x % k == 0:
			return False
	return True

def fastPower(x, n):
	#precondition:  x is a number, n is an integer.
	#postcondition:  returns x to the nth power (do not use **)
	#using the fastPower algorithm described below
	if n%2 == 0:
		return pow(x*x, n/2)
	else:
		return x*pow(x*x, n/2)

def allSubsets(x):
	#precondition:  x is a list of distinct elements (a set)
	#postcondition:  returns a list of all 2**n subsets of x
	return [[]]

def allPermutations(x,n):
	#precondition: x is a list
	#postcondition:  returns all possible orderings of the list x
	#as a list of lists.  
	return [[1]]

def allSubsetsOfSize(n,k):
	#precondition: k, n ints, 0 <= k <=n
	#postcondition:  returns all subsets of size k out of a
	#set of size n
	return [[]]

def allPermutationsOfSize(x,n):
	#precondition: x is a list
	#postcondition:  returns all possible orderings of the list x
	#as a list of lists.  
	return [[1]]

def depth(x):
	#x is a list (possibly nested)
	#returns the depth of the most highly nested element
	pass

def ecuder(f, list, start):
	#f is a function of two args, list is a list, start is a value
	#recursive implementation of reduce
	#write reduce using recursion
	pass

def sumfrom(n, x):
	#precondition: n is an integer
	#postcondition:  x is an integer list
	#return a sublist from x that adds to n; return False if this
	#fails to exist
	return []

def primeFactors(n):
	#n is an positive integer
	#return a list in ascending order of the prime factors of n, ignoring
	#repeats
	#primeFactorization(240) -> [2, 3, 5]
	pass

def primeFactorization(n):
	# n is a positive integer
	#return a list of two-element lists; the first element is a
	#prime factor of n, the second is the power of that factor.  
	#sample
	#primeFactorization(240) -> [[2, 4], [3, 1], [5, 1]]
	pass


print "extractAtoms([1,2,[3],[4,5,[6]]]) = ", extractAtoms([1,2,[3],[4,5,[6]]]), "expected: [1,2]"
print "extractAtoms([[[4,3],[1,7]],3,7,[3,8],98]) = ", extractAtoms([[[4,3],[1,7]],3,7,[3,8],98]), "expected: [3,7,98]"
print "extractAtoms([[2],a,<-...->,s]) = ", extractAtoms([[2],"a",[["hello"],"yes"],"t","o",["m"],[["m","s"]],"m",["s"],"s"]), "expected: [a,t,o,m,s]"

print

print "isPrime(113) = ", isPrime(113), "expected: True"
print "isPrime(7)", isPrime(7), "expected: True"
print "isPrime(8)", isPrime(8),"expected: False"

print

print fastPower(2,3)
print fastPower(2,4)
