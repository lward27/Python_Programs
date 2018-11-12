#precondition:   r is a nonnegative number
#postcondition:  returns the volume of a sphere with radius r.
def sphereVolume(x):
        return (3.14*(x**3))*4/3
print "sphereVolume(10) = ", sphereVolume(10), "expected: 4186.667"
print "sphereVolume(23) = ", sphereVolume(23), "expected: 50939.173333"
