#################################################################
#  
#    Author:  Lucas Ward
#    Date:    January 23rd, 2008
#    Program: Problem Set 2
#    Program Name:  wardlPS2.py
#
#################################################################
#precondition:   x is is an number
#postcondition:  returns x if x < 0, x*x if 0 <= x <= 3
#and sqrt(x) otherwise.
def piecewise(x):
	x = float(x)
	if x < 0:
		return x
	elif 0 <= x <= 3:
		return x*x
	else:
		return x**.5

#preconition:   x is a decimal integer
#postcondition:  returns the sum of the digits of x, using a 
#while loop
def sumDigitsIter(x):
	if x < 0:
		print "please type a positive integer"
	else:
		x = list(str(x))
		twaddle = 0
		k = 0
		while k < len(x):
			twaddle = twaddle + int(x[k])
			k += 1
		return twaddle

#precondition:   x is a decimal integer
#postcondition:  returns the sum of the digits of x, using 
#recursion.  
def sumDigitsRec(x):
	x = list(str(x))
	total = 0
	for k in range(0, int(len(x))):
		total += int(x[k])
	return total

#prec:  n is a positive integer
#postc:  return true if n is prime and false otherwise
#example:  isPrime(1) -> False  isPrime(7) -> True isPrime(4) -> False
#suggested algorithm:  check for divisibility by 2.  If the number
#is an even number bigger than 2, return False.  Otherwise
#check odd numbers 23,5,7.... 
#if you find no divisibility before sqrt(n), you know n is prime.
def isPrime(n):
	if n == 1:
		return False
	for k in range (2, int(n**0.5)+1):
		if n % k == 0:
			return False
	return True

#prec:  n is a nonnegative integer
#postc:  returns a list of the prime factors of n
def primeFactorization(n):
	if n < 0:
		n = -n
	if n % 2 == 0:
		return 2
	d = 3
	while d*d <=n:
		if n % d == 0:
			return d
		d += 2
	return n
def primeFactorization1(n):
	list = []
	while n > 1:
		wardl = primeFactorization(n)
		list.append(wardl)
		n /= wardl
	return list
#example:  primeFactorization(36) -> [2,2,3,3]
	

#prec:  n is an integer, x is a decimal number 
#postc:  returns x**n (do not use **) using recursion
#hint: use an if statement to detect a negative exponent.
#Obviate the negative exponent so you can just work on 
#the nonnegative case.
def powerRec(x,n):
	if n < 0:
		n = -n
		x = 1.0/x
	if n == 0:
                return 1
        return x*powerRec(x, n-1)

#prec:  n is an integer, x is a decimal number 
#postc:  returns x**n (do not use **) using recursion
#hint: use an if statement to detect a negative exponent.
#Obviate the negative exponent so you can just work on 
#the nonnegative case.
def powerIter(x,n):
	total = 1
	if n < 0:
		n = -n
		x = 1.0/x
	product = 1
	for k in range(n):
		product *= x
	return product

#prec:  n is a positive integer
#postc: returns true if n is the sum of its proper divisors
def isPerfect(x):
	list = []
	while x > 1:
		booger = primeFactorization(x)
		list.append(booger)
		x /= booger
		getlist = {}.fromkeys(list)
		newlist = getlist.keys()
		newlist = newlist + [1]
		total = 0
		k = 0
		while k < len(newlist):
			total = total + newlist[k]
			k += 1
	return total ## total for x = 6 is 6 but it returns false...?
	if total == x:
		return true

#prec:  x is a list
#postc:  reverse the list x in-place
#do not use built-in reverse method.
def reverseList(x):
	list = []
	if x==[]:
		return[]
	for i in range(len(x)-1,-1,-1):
		list.append(x[i])
	return list

##################################################
##############main routine (where tests suites go#
##################################################

print

print "piecewise(-3) = ", piecewise(-3), "expected: -3.0"
print "piecewise(2) = ", piecewise(2), "expected: 4.0"
print "piecewise(16) = ", piecewise(16), "expected: 4.0"

print

print "sumDigitsIter(234) = ", sumDigitsIter(234), "expected: 9"
print "sumDigitsIter(-234) = ", sumDigitsIter(-234), "expected: none"
print "sumDigitsIter(234104342) = ", sumDigitsIter(234104342), "expected: 23"

print

print "sumDigitsRec(234) = ", sumDigitsRec(234), "expected: 9"
print "sumDigitsRec(9999) = ", sumDigitsRec(9999), "expected: 36"
print "sumDigitsRec(101) = ", sumDigitsRec(101), "expected: 2"

print

print "isPrime(8) = ", isPrime(8), "expected: False"
print "isPrime(13) = ", isPrime(13), "expected: True"
print "isPrime(113) = ", isPrime(113), "expected: True"

print

print "primeFactorization1(995) = ", primeFactorization1(995), "expected: [5, 199]"
print "primeFactorization1(1000) = ", primeFactorization1(1000), "expected: [2,2,2,5,5,5]"
print "primeFactorization1(36) = ", primeFactorization1(36), "expected: [2,2,3,3]"

print

print "powerRec(5,-2) = ", powerRec(5,-2), "expected: .04"
print "powerRec(9,2) = ", powerRec(9,2), "expected: 81"
print "powerRec(6,3) = ", powerRec(6,3), "expected: 216"

print

print "powerIter(2,3) = ", powerIter(2,3), "expected: 8"
print "powerIter(3,0) = ", powerIter(3,0), "expected: 1"
print "powerIter(6,2) = ", powerIter(6,2), "expected: 36"

print

print "isPerfect(5) = ", isPerfect(6), "expected: True"
print "isPerfect(6) = ", isPerfect(6), "expected: True"
print "isPerfect(7) = ", isPerfect(6), "expected: True"

print

print "reverseList([1,2,3]) = ", reverseList([1,2,3]), "expected: [3,2,1]"
print "reverseList([6,2,3,8]) = ", reverseList([6,2,3,8]), "expected: [8,3,2,6]"
print "reverseList([3,2,1]) = ", reverseList([3,2,1]), "expected: [1,2,3]"
