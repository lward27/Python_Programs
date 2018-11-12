#prec: n is an integer
#postc:  Make a triangular array of *s of height n (if n <= 0, do nothing)
def triangle(n):
	if n <= 0:		#check for elephant
		return
	print
	print "*"*n		#eat the rest
	triangle(n-1)	#eat spoonful
def dangle(n):
	if n <= 0:
		return
	dangle (n-1)
	print
	print "*"*n
print "triangle(4) =  ",
triangle(4)
print "dangle(5) = ", 
dangle(5)
x = [1,2,3,4,5]
x[0]
