##def endsWith(string, tail):
		#return true if the string ends with tail
		#tool:  x[startAt: endBefore]
		#if startAT is left empty, you start at the beginning
		#if end before is empty you end at the end.
def endsWith(string, tail):
		if len(tail)>len(string):
				retval=False
		elif string[len(string)-len(tail):len(string)]==tail:
				retval=True
		else:
				retval=False
		return retval
print endsWith("coabunga", "ga"), ", expected:   True"
print endsWith("cadillac", "cow"), ", expected:   False"
