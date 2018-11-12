#prec:  days, hourse, minutes, seconds are nonnegative integers
#postc: returns thhe total number of seconds elapsed in the given time.
def seconds(days, hours, minutes, seconds):
		a = days*86400
		b = hours*3600
		c = minutes*60
		d = seconds
		return (a+b+c+d)
print "seconds(3, 3, 7, 6) = ", seconds(3, 2, 67, 6), "expected: 270426"
print "seconds(1, 6, 9, 58) = ", seconds(1, 6, 9, 58), "expected: 108598"
print "seconds(1000, 23, 59, 59) = ", seconds(1000, 23, 59, 59), "expected: 86486399"
