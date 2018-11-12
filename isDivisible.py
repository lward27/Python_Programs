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
print "isDivisible(8, 4) = ",
isDivisible(8, 4),
print "expected: true"
print "isDivisible(7, 4) = ",
isDivisible(7, 4),
print "expected: false"
print "isDivisible(1, 4) = ",
isDivisible(1, 4),
print "expected: false"
