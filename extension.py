#precondition:  filename has an extension
#postcondition:  returns the extension of the file without the period.
def getExtension(filename):
        #find the last period
        lastPeriod = filename.rfind(".")
        #move over one
        lastPeriod += 1
        return filename [lastPeriod:]
#testsweet
print "getExtension(\"cow.cpp\") = ", getExtension("cow.cpp"),  "expected: cpp"
print "getExtension(\"moose.cpp\") = ", getExtension("moose.cpp"),  "expected: cpp"
