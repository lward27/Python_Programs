#prec: roast is a string
#prec: bacon is a single character.
#examples:
#lard("moose", "z") -> ["zmoose", "mzoose, "mozose",
#	"moozse", "moosze", "moosez"]
import sys
def lard(roast, bacon):
	tally = []
	k = 0
	for k in range(len(roast)+1):
		tally.append(str(roast[0:k] + bacon + roast[k:]))
	return tally
def jumble(word):
	if len(word) <= 1:
		return [word]
	out = []
	first = word[0]
	rest = word[1:]
	blob = jumble(rest)
	for k in blob:
		out += lard(k, first)
	return out
input = raw_input("enter a word you wish to annanize",  )
mess = jumble(input)
mess.sort()
print mess
