#ask user for two numbers
#tell user quotient
#if the user enters a zero divisor tell him he is an idiot.
def divide(dividend, divisor):
		return float(dividend)/divisor
dividend = input("enter a dividend:   ")
divisor = input("enter a divisor:   ")
if divisor != 0:
		print "The quotient is "+ str(divide(dividend, divisor))+ "."
else:
		print "End user, thou art an IDIOT!"
