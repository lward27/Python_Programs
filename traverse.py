def printList(x):
		if x == []:    ## of len(x) == 0
				return
		first = x[0]
		rest = x[1:]
		print first,
		printList(rest)

x= [1,2,3,4,5,6,7,8,9]
printList(x)

print

print x[0]
print x[1]
print x[2]
print x[3]
print x[4]
