# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:17:54 2015

@author: nathaniel

This class is responsible for generating the markov chain.
It contains the necessary frequency dictionaries and functions, and that's it.
It is to be trimmed down version of the markov chain that
has only the essential components for generating the chain.

To train (create the dictionaries) look at chain_trainer.py.

"""


import random


class markov_state():
	def __init__(self, config_type, first_words, first_order, second_order):
		self.config = config_type
		self.first_words = first_words
		self.first_order = first_order
		self.second_order = second_order
		
		self.category = 'none yet'


	def buildChain(self, length=50):
		#these are the seed words
		first_word = self.getNextWord(self.first_words)
		second_word = self.getNextWord(self.first_order[first_word])

		newText = first_word + " " + second_word

		for _ in range(length-2):
			newD = self.merge(self.first_order[first_word], self.second_order[second_word])
	  
			first_word = second_word	
			second_word = self.getNextWord(newD)
		  
			newText += " " + second_word
		return newText


	def merge(self,list1, list2):
		''' merges two dictionaries into 3rd ''' 
		''' why multiplies counts instead of adds? '''
		
		newDict = dict()
		union_keys = set(list1.keys()).union(set(list2.keys()))
		for each in union_keys:
			newDict[each] = (list1[each] if each in list1.keys() else 1) * \
				(list2[each] if each in list2.keys() else 1)

		#print("List1:%s\nList2:%s\nNewList:%s"%(list1, list2, newDict))
		return newDict

	def getNextWord(self, newD):
		''' Given a dictionary of words and frequencies, 
		this will generate a new word by random number '''
		
		possibles = []
		
		#flatmap the dictionary out
		for (a,b) in zip(newD.keys(), newD.values()):
			possibles += [a]*b 
	
		success = 0

		#this type of checking is not my favorite style
		#when we know why owa (maybe others) are causing problems,
		#we can get rid of this block.
		while(success == 0):

			#choose a random element in the list
			index = random.randint(0, len(possibles)-1)
			word = possibles[index]	

			#make sure this word is legit
			try: 
				self.first_order[word]
				self.second_order[word]
				success = 1
			except:
				success = 0

		return word








		
