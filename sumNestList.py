stuff = [1,2,[3,4,[5,[6,7],[8,9],10],[11,12,13]],14]
def sumTreeEntries(tree):
	if(type(tree) != type([])):
		return tree
	##we know it's a list
	return sum(map(sumTreeEntries, tree))
