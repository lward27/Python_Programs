def square(x):
        return x*x
def cube(x):
        return x*square(x)
def fourth(x):
        return x*cube(x)
def fourth1(x):
        return square(X)*square(x)
print "square (10) = ", square(10), "expected: 100"
print "square (-3) = ", square(-3), "expected: 9"
print "cube (-3) = ", cube(-3), "expected: -27"
print "cube (8) = ", cube(-8), "expected: -512"
print "fourth (2) = ", fourth(2), "expected: 16"
