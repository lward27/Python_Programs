def minSec(secs):
		min = secs/60
		sec = secs%60
		return (min, sec)   ##returning a 2-tuple
secs = input("Enter a number of seconds:   ")
ms = minSec(secs)
#print ms
print "you entered", secs, "seconds."
print "That\'s", ms[0], "minutes and ", ms[1], "seconds"
