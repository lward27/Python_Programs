def bankAccount(n, r, k, p):
		return p*((1 + (r/k))**(k*n))
r = input("enter a interest rate in decimal form:   ")
k = input("enter the compounding factor per year:   ")
n = input("enter number of years:   ")
p = input("enter initial balance:   ")
if r != 1:
		print "the amount of money after", n, "years is "+ str(bankAccount(n, r, k, p))+ "."
else:
		print "this account gains no money you fag."
