#prec:  secs is an integer
#post:  return a tuple (days, hours, min, sec) so that
# 0 <= sec < 60
# 0 <= min < 60
# 0 <= hr < 24
#for example, secs(3800) returns (0,1,3,20)
###Hint:  % is your friend!
def dhms(secs):
		day = secs/86400
		secs=secs%86400
		hour = secs/3600
		secs=secs%3600
		min = secs/60
		secs=secs%60
		sec = secs
		return (day, hour, min, sec)
secs = input("Enter a number of seconds:   ")
ds = dhms(secs)
print "you entered", secs, "seconds."
print "Thats", ds[0], "days and ", ds[1], "hours and ", ds[2], "minutes and ", ds[3], "seconds"
