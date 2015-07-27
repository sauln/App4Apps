# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:17:54 2015

@author: nathaniel




"""

import random


class markov_state():
    def __init__(self, config_type, first_words, first_order, second_order):
        self.config = config_type
        self.first_words = first_words
        self.first_order = first_order
        self.second_order = second_order
        
        
        
        
    def buildChain(self, length):
    	#these are the seed words
    
        first_word = self.getNextWord(self.first_words)
        second_word = self.getNextWord(self.first_order[first_word])
        	
        newText = first_word + " " + second_word
        
        for _ in xrange(length):
            newD = self.merge(first_word, second_word)
            		
            first_word = second_word	
            second_word = self.getNextWord(newD)
            			
            newText += " " + second_word
        return newText



		
    def merge(self, word2, word1):
        ''' This will merge the first and second order dictionaries of the specific words'''
        newD = self.mergeLists(self.first_order[word1], self.second_order[word2])
        return newD
    

	
	
    def mergeLists(self,list1, list2):
        newDict = dict()
        ''' create a new dictionary of frequencies based of two inputs ''' 
       
        for each in list1:
            if each in list2:
                newDict[each] = list1[each]*list2[each]
        return newDict
	

    def getNextWord(self, newD):
        ''' Given a dictionary of words and frequencies, 
        this will generate a new word by random number '''
        
        
        #TODO this is so naive it is borderline moronic
        total = 0
        newTotal = 0
        
        for each in newD:
            total += newD[each]
            
        index = random.randint(1, total)
    	
        for each in newD:
            newTotal += newD[each]
            if newTotal >= index:
                 return each
			
			
		