
#this module will take a markov transition dictionary and build a chain from it.

import random



def buildChain(firstOrder, secondOrder, first):
	#these are the seed words

	firstWord = getNextWord(first)
	secondWord = getNextWord(firstOrder[firstWord])
	
	newText = firstWord + " " + secondWord

	for _ in xrange(45):
		newD = merge(firstOrder,  secondOrder, firstWord, secondWord)
		
		firstWord = secondWord	
		secondWord = getNextWord(newD)
			
		newText += " " + secondWord
		
	return newText

		
		
def getNextWord(newD):
	''' Given a dictionary of words and frequencies, 
	this will generate a new word by random number '''
	total = 0
	newTotal = 0

	
	for each in newD:
		total += newD[each]
		
	
	index = random.randint(1, total)
	
	
	for each in newD:
		newTotal += newD[each]
		if newTotal >= index:
			return each
			
			
		
def merge(firstOrder, secondOrder, word2, word1):
	''' This will merge the first and second order dictionaries of the specific words'''
	newD = mergeLists(firstOrder[word1], secondOrder[word2])
	return newD


	
	
def mergeLists(list1, list2):

	newDict = dict()
	''' create a new dictionary of frequencies based of two inputs ''' 
	#so naive
	
	
	
	for each in list1:
		if each in list2:
			newDict[each] = list1[each]*list2[each]
			
	
	return newDict
	

	
	
	
	
	

