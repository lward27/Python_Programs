def printList(someList):
		if len(someList) == 0:
				return
		first = someList[0]
		rest = someList[1:]
		print first
		printList(rest)
x = range(1,100)
printList(x)
