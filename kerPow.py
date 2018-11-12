def kerPow(x, n):
	print "babies!!!!"
	if n == 0:
		return 1
	if n % 2 == 0:
		return kerPow(x*x, n/2)
	return x*kerPow(x*x,n/2)
print kerPow(1.000000001,1000000000)
