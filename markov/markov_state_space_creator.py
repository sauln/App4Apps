# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 18:40:53 2015

@author: nathaniel





attempting to rewrite the markov chain



"""


class markov_state_space():
    def __init__(self, category):
        
        
        
        print "set up Text"
        text = self.setupText(category)
        print text
        
        print "strip erroneous characters"
        text_2 = self.strip_all(text)
        
        print "gather first words of sentences"
        self.first_words = self.gather_firsts(text_2)
        
        print "generate first and second order dictionaries"
        self.first_order, self.second_order  = self.make_dictionaries(self.first_words, text_2)
        
        
    def setupText(self, category):
        f_cat = "corpus_" + category + ".txt"
        try:
            f = open('../../home/saulgill/saulgill-site/corpus/'+ f_cat, 'r')
        except:
            f = open('../corpus/' + f_cat, 'r')
            pass
        	
        txt = f.read()
        return txt
        
    def strip_all(self, text):
        print "NOT YET IMPLEMENTED: remove all the erroneous characters"
        return text




    def gather_firsts(self, text):
        firstLetters = []
        
        #split by sentences
        sentences = text.lower().split('.')
        #add just the first words of each sentence
        for each in sentences:
            each = each.split()
        try:
            firstLetters.append(each[0])
        except:
            pass
        
        return firstLetters
        
        
        
        
    def make_dictionaries(self, first_words, text):
        print "this is the hard part"
        return "a", "b"
        
        
        


	#first = self.makeDicts(self.firstOrder, self.secondOrder, text, first)
	print "finished"
        





