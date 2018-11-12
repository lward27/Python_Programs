def isDigit(ch):
	if len(ch) != 1:
		return False
	return ch in "0123456789"
def condonw(ch):
		return (len(ch) == 1) and (ch in "0123456789")
def isZipCode(code):
	if len(code) != 5:
		return False
	for k in code:
		if not(isDigit(k)):
			return False
	return True
