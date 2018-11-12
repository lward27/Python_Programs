from math import *
def introduction(x):
	#area of square
	if enter is "a":
		b = input("Enter the length of one side of the square:  ")
		new = b**2.
		print "The area of the square is:",new
	#area of rectangle	
	elif enter is "b":
		l = input("Enter the length of one side of the rectangle:  ")
		w = input("Enter the width of one side of the rectangle:  ")
		new = w*l*1.
		print "The area of the rectangle is:",new
	#area of triangle
	elif enter is "c":
		b = input("Enter the length of the base of the triangle:  ")
		h = input("Enter the height of the triangle:  ")
		new = .5*b*h
		print "The area of the triangle is:",new
	#area of parallelogram
	elif enter is "d":
		b = input("enter the length of the base of the parallelogram:  ")
		h = input("enter the height of the parallelogram:  ")
		new = b*h*1.
		print "The area of the Parallelogram is:",new
	#area of trapezoid
	elif enter is "e":
		h = input("enter the altitude of the trapezoid:  ")
		b = input("enter the length of base 1:  ")
		B = input("enter the lenght of base 2:  ")
		new = h*((b + B) / 2.)
		print "The area of the trapezoid is:",new
	#area of circle
	elif enter is "f":
		r = input("enter the radius of the circle:  ")
		new = (22/7.)*(r**2)
		print "The are of the circle is:",new
	#circumference of circle
	elif enter is "g":
		d = input("enter the diameter of the circle:  ")
		new = (22/7.)*d
		print "The circumference of the circle is:",new
	#hypotenuse of triangle
	elif enter is "h":
		a = input("enter the length of the shortest side:  ")
		b = input("enter the length of the adjacent side, not the hypotenuse:  ")
		new = sqrt((a**2)+(b**2.))
		print "The hypotenuse of the triangle is:",new
	#area of rectangle prism
	elif enter is "i":
		l = input("enter the length of the Rectangular Prism:  ")
		w = input("enter the width of the Rectangular Prism:  ")
		h = input("enter the height of the Rectangular Prism:  ")
		new = l*w*h*1.
		print "The volume of the rectangular prism is:",new
	#volume of cube
	elif enter is "j":
		e = input("enter the length of one side of the cube:  ")
		new = e**3.
		print "The volume of the cube is",new
	#volume of cylinder
	elif enter is "k":
		r = input("enter the radius of the base of the cylinder:  ")
		h = input("enter the height of the cylinder:  ")
		new = ((22/7.)*(r**2))*h
		print "The volume of the cylinder is",new
	#volume of cone
	elif enter is "l":
		r = input("enter the radius of the cone:  ")
		h = input("enter the height of the cone:  ")
		new = (1/3.)*(22/7)*(r**2)*h
		print "The volume of the cone is",new
	#volume of triangluar prism
	elif enter is "m":
		b = input("enter the length of the base of the base triangle:  ")
		h = input("enter the height of the base of the base triangle of the triangluar prism:  ")
		H = input("enter the height of the triangluar prism:  ")
		new = ((1/2.)*b*h)*H
		print "The volume of the triangular prism is:",new
	#volume of sphere
	elif enter is "n":
		r = input("enter the radius of the sphere:  ")
		new = (4/3.)*(22/7)*(r**3)
		print "The volume of the sphere is:",new

enter = raw_input("choose a formula:\n(a) Area of Square\n(b) Area of Rectangle\n(c) Area of Triangle\n(d) Area of Parallelogram\n(e) Area of Trapezoid\n(f) Area of Circle\n(g) Circumference of Circle\n(h) Pythagorean Theorem\n(i) Rectangular Prism Volume\n(j) Cube Volume\n(k) Cylinder Volume\n(l) Cone Volume\n(m) Triangular Prism Volume\n(n) Spere Volume\n")
introduction(enter)
