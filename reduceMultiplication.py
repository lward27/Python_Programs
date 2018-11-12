def prod(x):
	return reduce(lambda x,y: x*y, x, 1)
print prod([1,2,3,4])
def pwr(base,exp):
	return reduce(lambda x,y: base*x, [0]*exp, 1)
print pwr(2,2)

#takes a list of strings and globs them into one big string.
#1,2,3,4
#start on 1
#1    3    6   7   
#     3    18  126    
