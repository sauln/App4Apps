import pickle


def load_markov_chain(category):
	mc =  pickle.load(open("markov/dictionaries/markov_business.p", encoding='utf-8'))
	return mc


def gen_new_chain(mc):
    return mc.buildChain()
    





