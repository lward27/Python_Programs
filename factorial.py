def factorial(n):
		##prec: n >= 0
		##postc: returns product of integers 1 - n (n included)
		if type(n) != int or n < 0:
				return "fuck head"
		elif n == 0:
				return 1
		return n*factorial(n-1)
n = 7
print factorial(n)
