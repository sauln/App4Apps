# -*- coding: utf-8 -*-


#import markov.transition_builder as tb
#import markov.chain_builder as chain

import pickle

import markov.markov_state_space_creator as ms_make
import markov.markov_state as ms




                
def test_dictionary(chain):
    for each in chain.first_words.keys():
        try:
            chain.first_order[each]
        except:
            print "stopped on ", each





categories = ["test", "business", "finance", "education"]


for each in categories:
    chain_creator = ms_make.markov_state_space(each)
    
    test_dictionary(chain_creator)
    
    markov_chain = ms.markov_state(chain_creator.category, chain_creator.first_words, 
                    chain_creator.first_order, chain_creator.second_order) 
                    
            
                    
    pickle.dump(markov_chain, open('dictionaries/markov_' + each + '.p','wb')) 



        
