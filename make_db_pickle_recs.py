from initdata import bob, sue, tom
import pickle
for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue), ('lou', lou)]:
	recfile = open(key+'.pkl', 'w')
	pickle.dump(record, recfile)
	recfile.close()
