#################################################################
#  
#    Author:  Lucas Ward
#    Date: January 11th, 2008   
#    Program: Problem Set 1
#    Program Name:  wardlPS1.py
#
#################################################################
#precondition:   x is is an integer
#postcondition:  returns True if x is even and False otherwsie
def isEven(x):
		return (x%2) == 0

#precondition:   r is a nonnegative number
#postcondition:  returns the volume of a sphere with radius r.
def sphereVolume(x):
		return (3.14*(x**3))*4/3

#prec:  x is a number
#postc:  returns the fractional part of the number
#example:  fracPart(4.5) = .5,  fracPart(-3.1) = .9
def fracPart(x):
		return 1 - (x%1)

#prec:  x is a nonnegative integer
#postc:  returns the sum of the last two digits of x
def sumOfLastTwoDigits(x):
		if x < 10:
				return "must be greater then ten!"
		list0 = list(str(x % 100))
		return int(list0[0]) + int(list0[1])

#prec:  x is an integer
#postc:  returns the first digit of x
def firstDigit(x):
		list0 = list(str(x))
		return int(list0[0])

#prec:  days, hourse, minutes, seconds are nonnegative integers
#postc: returns thhe total number of seconds elapsed in the given time.
def seconds(days, hours, minutes, seconds):
		a = days*86400
		b = hours*3600
		c = minutes*60
		d = seconds
		return (a+b+c+d)

#prec: dividend, divisor are integers; divisor is not zero
#postc:  return True if divisor divides dividend evenly.
def isDivisible(dividend, divisor):
		value = str(float(dividend)/divisor)
		lastPeriod = value.rfind(".")
		lastPeriod += 1
		value2 = value [lastPeriod:]
		if value2 == '0':
		        print "true"
		else: print "false"

#prec:  moe, larry, joe are integers
#post:  returns true if moe < larry <= joe.
def isIncreasing(moe, larry, joe):
		if moe < larry <= joe:
				print "true"
		else: print "false"

#prec:  secs is an integer
#post:  return a tuple (days, hours, min, sec) so that
# 0 <= sec < 60
# 0 <= min < 60
# 0 <= hr < 24
#for example, secs(3800) returns (0,1,3,20)
###Hint:  % is your friend!
def dhms(secs):
		day = secs/86400
		secs=secs%86400
		hour = secs/3600
		secs=secs%3600
		min = secs/60
		secs=secs%60
		sec = secs
		return (day, hour, min, sec)

##################################################
##############main routine (where tests suites go#
##################################################
print

print "isEven(34) = ", isEven(34), "expected:  true"
print "isEven(3) = ", isEven(33), "expected: false"
print "isEven(1467) = ", isEven(31), "expected: false"

print

print "sphereVolume(10) = ", sphereVolume(10), "expected: 4186.667"
print "sphereVolume(23) = ", sphereVolume(23), "expected: 50939.173333"
print "sphereVolume(2) = ", sphereVolume(2), "expected: 33.4933333333"

print

print "fracPart(5.5) = ", fracPart(5.5), "expected: .5"
print "fracPart(56.78) = ", fracPart(56.78), "expected: .22"
print "fracPart(-12.2) = ", fracPart(-12.2), "expected: .2"

print

print "sumOfLastTwoDgits(456) = ", sumOfLastTwoDigits(456), "expected: 11"
print "sumOfLastTwoDgits(1000000098) = ", sumOfLastTwoDigits(1000000098), "expected: 17"
print "sumOfLastTwoDgits(5) = ", sumOfLastTwoDigits(5), "expected: look left, read."

print

print "firstDigit(234643) = ", firstDigit(234643), "expected: 2"
print "firstDigit(4) = ", firstDigit(4), "expected: 4"
print "firstDigit(9999999) = ", firstDigit(9999999), "expected: 9"

print

print "seconds(3, 3, 7, 6) = ", seconds(3, 2, 67, 6), "expected: 270426"
print "seconds(1, 6, 9, 58) = ", seconds(1, 6, 9, 58), "expected: 108598"
print "seconds(1000, 23, 59, 59) = ", seconds(1000, 23, 59, 59), "expected: 86486399"

print

print "isDivisible(8, 4) = ",
isDivisible(8, 4),
print "expected: true"
print "isDivisible(7, 4) = ",
isDivisible(7, 4),
print "expected: false"
print "isDivisible(1, 4) = ",
isDivisible(1, 4),
print "expected: false"

print

print "isIncreasing(1, 2, 3) = ",
isIncreasing(1, 2, 3)
print "expected: true"
print "isIncreasing(4, 2, 3) = ",
isIncreasing(4, 2, 3)
print "expected: false"
print "isIncreasing(-99, -3, 1004) = ",
isIncreasing(-99, -3, 1004)
print "expected: true"

print

print "dhms(86410) = ", dhms(86410), "expected: (1,0,0,10)"
print "dhms(3723) = ", dhms(3723), "expected: (0,1,2,3)"
print "dhms(0) = ", dhms(0), "expected: (0,0,0,0)"
