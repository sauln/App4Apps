
from app4apps.training.markov import chain

mc = dict()
mc["business"] = chain.load_markov_chain("business")
mc["finance"]  = chain.load_markov_chain("finance")
mc["education"] = chain.load_markov_chain("education")



