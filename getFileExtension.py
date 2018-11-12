#precondition:  filename has an extension
#postcondition:  returns the extension of the file without the period.
def lengthSquared(someString):
		x = len(someString)
		return x*x
#prec:  someString is a string
#postc:  returns True if someString has three or more characters
def hasThreeCharacters(someString):
		return len(someString) >= 3
##Test suite (test sours)
print "square (10) = ", square(10), "expected: 100"
print "square (-3) = ", square(-3), "expected: 9"
print "cube (-3) = ", cube(-3), "expected: -27"
print "cube (8) = ", cube(-3), "expected: 512"
print "fourth (2) = ", fourth(2), "expected: 16"
print "lengthSquared(\"i like cheese\") = ", lengthSquared("i like cheese")
print "hasThreeCharacters(\"kerfuffle\") = ", hasThreeCharacters("kerfuffle")
print "hasThreeCharacters(\"io\") = ", hasThreeCharacters("io")
