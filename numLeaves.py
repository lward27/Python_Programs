from BinaryTree import *

def numLeave(x):
	if x == EMPTY:
		return 0
	if x.left == EMPTY and x.right == EMPTY:
		return 1
	return numLeave(x.left) + numLeave(x.right)

x = makeTree([1,2,3,4,5,6,7,8,9])
print x
print numLeave(x)
