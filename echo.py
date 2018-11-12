#prec:  someString is a string
#times is a integer
#postc:
#prints someString times times to the screen
#if times <=0, nothing prints.
def repeat(someString, times):
	if times <= 0:
		return
	print someString
	repeat(someString, times - 1)
