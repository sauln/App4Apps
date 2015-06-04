""" 
Prototype for second order markov chain generator..
Nathaniel Saul and Miles Saul

TODO:
first word, ending word,  varying weights for words throughout a sentence.
"""






import random
def main():
	firstOrder = dict()
	secondOrder = dict()
	first, text = setupText()
	first = makeDicts(firstOrder, secondOrder, text, first)
	print buildChain(firstOrder, secondOrder, first)

	


''' These functions will setup the feedstock'''







''' These functions will build the chain ''' 

	
	
	



	
	
	
''' These functions will build the dictionary '''


	#toFreqDict(first)






	
	



		#d1 = dict()
		#print type(firstOrder)
		#print type(firstOrder["taylor"])
		#for eachK, eachV in zip(firstOrder.keys(), firstOrder.values()):
		#	firstOrder[eachK] = {x:eachV.count(x) for x in eachV}

	


if __name__ == '__main__':
    main() 



