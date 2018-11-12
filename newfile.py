def abs(x):
	return x if x >= 0 else -x
def muck(n):
	return n*muck(n-1) if n > 1 else 1
