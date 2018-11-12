############################################################
#
#     Frac.py
#     Author: John Morrison
#     This is a class that enables Python to manipulate
#     rational numbers.   Both denominator and numerator are
#     arbitrary precision.
#     Last modified:  8 Feb 2008
#     
############################################################

class Frac:
	def __init__(self, _num = 0, _denom = 1):
		self.num = _num/self.gcd(_num, _denom)
		self.denom = _denom/self.gcd(_num, _denom)
		if self.denom < 0:
			self.num = -self.num
			self.denom =  -self.denom
		##called to print a fraction            
	def __str__(self):
		if self.denom == 1:
			return str(self.num)
		return str(self.num) + "/" + str(self.denom)
        
	def gcd(self, x, y):
		if x < 0:
			x = -x
		if y < 0:
			y = -y
		while x > 0:
			x,y = y%x, x
		return y
	##overload +
	def __add__(self, other):
		if(type(other)==type(1)):
			other = Frac(other,1)
		top = (self.num * other.denom) + self.denom* other.num
		bottom = self.denom* other.denom
		return Frac(top, bottom)

	def __radd__(self, other):
		if(type(other)==type(1)):
			other = Frac(other,1)
		top = (self.num * other.denom) + self.denom* other.num
		bottom = self.denom* other.denom
		return Frac(top, bottom)

	def __iadd__(self, other):
		if(type(other)==type(1)):
			other = Frac(other,1)
		top = (self.num * other.denom) + self.denom* other.num
        	bottom = self.denom* other.denom
        	return Frac(top, bottom)
		#overload -
	def __sub__(self, other):
		if(type(other)==type(1)):
			other = Frac(other,1)
		top = (self.num * other.denom) - self.denom* other.num
		bottom = self.denom* other.denom
		return Frac(top, bottom)

	def __isub__(self, other):
		if(type(other)==type(1)):
			other = Frac(other,1)
		top = (self.num * other.denom) - self.denom* other.num
		bottom = self.denom* other.denom
		return Frac(top, bottom)
		#overload *
	def __mul__(self, other):
		if(type(other)==type(1)):
			other = Frac(other,1)
		top = self.num*other.num
		bottom = self.denom*other.denom
		return Frac(top, bottom)

	def __rmul__(self, other):
		if(type(other)==type(1)):
			other = Frac(other,1)
		top = self.num*other.num
		bottom = self.denom*other.denom
		return Frac(top, bottom)

	def __imul__(self, other):
		if(type(other)==type(1)):
			other = Frac(other,1)
		top = self.num*other.num
		bottom = self.denom*other.denom
		return Frac(top, bottom)
	#overload /
	def __div__(self, other):
		if(type(other)==type(1)):
			other = Frac(other,1)
		top = self.num *other.denom
		bottom = self.denom * other.num
		return Frac(top, bottom)

	def __idiv__(self, other):
		if(type(other)==type(1)):
			other = Frac(other,1)
		top = self.num *other.denom
		bottom = self.denom * other.num
		return Frac(top, bottom)
	#overload <, <= etc
	def __cmp__(self, other):
		return cmp(self.num*other.denom, self.denom*other.num) 

	def __pow__(self, n):
		return Frac(self.num**n, self.denom**n)
		#cast to integer
	def __int__(self):
		return self.num/self.denom
		#make floating point representation
	def __float__(self):
		floatMax = 2**1023 - 1
		n = 15
		sign = 1
		if self.num < 0:
			sign = -1
			self.num = -self.num
		topmag = len(str(self.num))
		botmag = len(str(self.denom))
		if(self.num > floatMax or self.denom > floatMax):
			exponent = topmag - botmag
			numMan = float(str(self.num)[0:n])
			denomMan = float(str(self.denom)[0:n])
			return sign*numMan/denomMan*(10**exponent)
		else:
			return float(self.num)/float(self.denom)*sign
		return 0
