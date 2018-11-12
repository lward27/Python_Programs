def isNumber(x):
	return x[0] in "0123456789"
def shavePunct(word):
	end = len(word) - 1
	begin = 0
	while word[begin] < "a" or word[begin] > "z":
		begin += 1
		if begin == len(word): return ""
	while word[end] < "a" or word[end] > "z":
		end -= 1
	return word[begin: end + 1]
lineNo = 1
inFilePipe = open("kjv12.txt", "r")
concordance = {}
for line in inFilePipe:
	line = line.lower()
	words = line.split()
	for k in words:
		if not isNumber(k):
			k = shavePunct(k)
			if k in concordance.keys():
				concordance[k] += 1
			else:
				concordance[k] = 1
inFilePipe.close()
outFilePipe = open("concordance.txt", "w")
for k in concordance.keys():
	outFilePipe.write(k + "\t\t" + str(concordance[k]) + "\n")
outFilePipe.close()
