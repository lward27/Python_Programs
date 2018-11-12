import re
def isDecimalDigit(str):
	seeker = re.compile("\d")
	return bool(seeker.search(string))
def isAlpha(string):
	seeker = re.compile("[a-zA-Z]")
	return bool(seeker.search(string))
