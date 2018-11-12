from isZipCode import *
##num is a string
##first char of num can be an optional + or -
##first numerical ch must be nonzero
##rest are digits 0-9.
def isDecimalInteger(num):
	finger = 0
	if num[0] in "+-":
		finger = 1
	num = num[finger:]	##slice off the sign
	if len(num) == 0:
		return False	##handle sign-only case
	elif len(num) == 1:
		return isDigit(num)
	elif (num[0] == 0):
		return False
	for k in num:
		if not(isDigit(k)):
			return False
	return True
