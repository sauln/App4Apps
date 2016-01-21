import pickle
import app4apps.training.markov.chain as chain
mc = dict()

categories = [ "business", "education", "finance"]

for each in categories:
	fin = open("app4apps/training/markov/dictionaries/markov_%s.dat"%each, 'rb')
	mc = pickle.load(fin)
	
	fin.close()


	try:
		print("Test if has category")
		print(mc.category)
	except:
		print("no category yet")



	print("adding category and pickling %s"%each)	
	fout = open("app4apps/training/markov/dictionaries/markov_%s.dat"%each, 'wb')
	mc.category = each
	
	
	try:
		print("Test if has category")
		print(mc.category)
	except:
		print("no category yet")
	
	
	
	pickle.dump(mc, fout)
	fout.close()


