def keepLonger(tooSmall, list1):
	type(list1) == type([])
	x = []
	for k in list1:
		if len(k) > tooSmall:
			x.append(k)
	return x
		
print keepLonger(2, ["h", "hi", "hey", "help", "hello"])
print keepLonger(3, ["h", "hippolite", "hey", "help", "word"])
