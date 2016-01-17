# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 23:11:49 2015

@author: nathaniel


this is the interface for the app4apps.

All it needs to do is load which dictionary it wants, and to build a new chain with that dictionary




"""

import pickle



def load_dictionary(category):
    try:
        f = pickle.load(open('../../home/saulgill/saulgill-site/markov/dictionaries/markov_'+category+'.p'))
    except:
        f = pickle.load(open('markov/dictionaries/markov_'+category+'.p'))
    return f 
    
def gen_new_chain(mc):
    return mc.buildChain()
    





