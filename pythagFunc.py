def hypot(a, b):
	return (a*a + b*b)**(.5)
leg1 = input("Enter a leg:   ")   #input gets a number
leg2 = input("Enter a leg:   ") 
print "You entered legs of length", leg1, "and", leg2
print "The hypoteneuse has length", hypot(leg1, leg2)
