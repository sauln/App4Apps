


from app4apps.training.markov import chain
from . import mc



def new_text(category):
	
	if (category in mc.keys()):
		return chain.text_from_chain(mc[category]) 
	else:
		return "This category is not supported"
	










