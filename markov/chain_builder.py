
#this module will take a markov transition dictionary and build a chain from it.





def buildChain(firstOrder, secondOrder, first):

	#these are the seed words
	firstWord = getNextWord(first)
	secondWord = getNextWord(firstOrder[firstWord])
	
	newText = firstWord + " " + secondWord

	for i in xrange(45):
		try:
			newD = merge(firstOrder,  secondOrder, firstWord, secondWord)
			
			
			firstWord = secondWord
			secondWord = getNextWord(newD)
			
			
			newText += " " + secondWord
		except:
			break
		#print secondWord

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
	list1 = firstOrder[word1]
	list2 = secondOrder[word2]
	
	newD = mergeLists(list1, list2)
	return newD


	
	
def mergeLists(list1, list2):


	newDict = dict()
	''' create a new dictionary of frequencies based of two inputs ''' 
	for each in list1:
		if each in list2:
			newDict[each] = list1[each]*list2[each]
			
	
	
	

	
	
	
	
	

