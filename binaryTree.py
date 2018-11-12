############################################################
#
#     BinaryTree.py
#     Author: Dennis Yeh
#     Corruptor: John Morrison
#     This is a class that enables Python to manipulate
#     binary trees.  
#     Last modified:  8 Feb 2008
#     
############################################################
EMPTY = None

class BinaryTree:
	linksOff = False
	def __init__(self, datum, top=EMPTY, bottom=EMPTY):
		self.datum = datum
		self.top  = top
		self.right = top
		self.bottom = bottom
		self.left = bottom
	def __str__(self):
		return toString(self)

def toString(tree, level=0):
	up,down = ('','') if BinaryTree.linksOff else ('  '*level+' /\n' , '  '*level+' \\\n')
	return '' if (tree == EMPTY) else toString(tree.top, level+1) + up +'  '*level+ str(tree.datum) + '\n' + down + toString(tree.bottom, level+1)

##pass a list and build a binary tree tinsel-style (Level
##order traversal).
def makeTree ( list , n=1 ) :
	return EMPTY if (n > len(list)) else BinaryTree( list[n-1] , makeTree( list , 2 * n ) , makeTree ( list, 2 * n + 1 )) 

jenny = makeTree([8,6,7,5,3,0,9])
joshua = makeTree([1,3,5,7,9,11,13,15,17,19])
##insert an object into binary search tree
def insertBST ( t , obj ) :
	if ( t == EMPTY ) :
		return BinaryTree(obj)
	elif ( obj < t.datum ) :
		return BinaryTree( t.datum , t.top , insertBST ( t.bottom , obj ) )
	else :
		return BinaryTree( t.datum , insertBST ( t.top , obj ) , t.bottom) 
##Make a BST with an entire list.
def makeBST ( list ) :
	newTree = EMPTY
	for x in list:
		newTree = insertBST ( newTree , x )
	return newTree

bst1 = makeBST ( [ 10 , 14 , 6 , 3, 17 , 9 , 11 , 1 , 8 , 16 , 7] )
bst2 = makeBST ( [ 4 , 6 , 8 , 9 , 5 , 2 , 3 , 1 , 7 ] )
