def isList(o):
	return type(o) == type([])
def printTree(item):
	if ( not isList(item)):
		print item
		return
	for k in item:
		printTree(k)



items = ["root", []]
items[1].append(["cats", []])
items[1].append(["birds", []])
items[1].append(["plants", []])
items[1][0][1].extend(["tiger", "lynx", "serval"])
items[1][1][1].extend(["swan", "ibis", "raven"])
items[1][2][1].extend(["orchid", "pansy"])

print items
printTree(items)
