##pre: x is a numerical list
##postc: sum of the list is returned.
def listSummerIter(x):
	twaddle = 0
	k = 0
	while k < len(x):
		twaddle = twaddle + x[k]
		k += 1
	return twaddle
def listSummerRec(x):
	if x == []:
		return 0;
	first = x[0]
	rest = x[1:]
	return first + listSummerRec(rest)



print listSummerRec([1,5,7,13])
print listSummerRec([])
