import pickle


def load_markov_chain(category):
	f = open("app4apps/training/markov/dictionaries/markov_business.p", 'rb')
	mc =  pickle.load(f)
	return mc


def text_from_chain(mc, length=50):
	return mc.buildChain(length)
    





