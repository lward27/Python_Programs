#precondition: word is a string
#postc: return True if word has three or more characters
def hasThreeChars(word):
		return len(word) >= 3
test = raw_input("Type a word:  ")
if hasThreeChars(test):
		print "you entered a string with at least 3 chars."
else:
		print "you entered a short string."
#test sweet, offset by ##
#print "hasThreeChars(\"Lucas\") = ", hasThreeChars("Lucas"), "expected: true"
#print "hasThreeChars(\"io\") = ", hasThreeChars("io"), "expected: false"
