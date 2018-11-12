def isList ( exp ) :
	return type(exp) == type([])
def isFlat(someList):
	for k in someList:
		if isList(k): return False
	return True
def nestSum(someList):
	if someList == []:
		return 0
	if (not isList(someList)):
		return someList
	return sum(map(nestSum, someList))	
def nestSum2(someList):
	if someList == []:
		return 0
	if (not isList(someList)):
		return someList
	first = someList[0]
	rest = someList[1:]
	return nestSum2(first) + nestSum2(rest)
def flatten(someList):
	if (not isList(someList)):
		return [someList]
	if isFlat(someList): return someList
	return (map(flatten, someList))

print isList([1,2,3])
print isFlat([1,2,3])
print nestSum([1,2,[5,6],3])
print nestSum2([1,2,[5,6],3])
print flatten([1,2,[3,4]])
