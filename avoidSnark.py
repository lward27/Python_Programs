import os.path
import sys
fn = sys.argv[1]
if os.path.isfile(fn):
	inPipe = open(fn, "r")
	for k in inPipe:
		print k,
		inPipe.close()
##put in os.path.isdir as an example
else:
	print "Purported file", fn, "does not exist, or you have called this program on a directory."
