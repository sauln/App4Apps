""" 

Prototype for second order markov chain generator..

Nathaniel Saul and Miles Saul

TODO:

first word, ending word,  varying weights for words throughout a sentence.



"""






import random
def main():


	firstOrder = dict()
	secondOrder = dict()

	text = setupText()


	#makeDicts(firstOrder, secondOrder, text)

	#buildChain(firstOrder, secondOrder)

	


''' These functions will setup the feedstock'''


def setupText():
	feedstock = readFile()
	text = prepareText(feedstock)

def readFile():
	f = open('taylor.txt', 'r')
	txt = f.read()
	return txt


def prepareText(txt):

	sent = txt.lower().split('.')


	first = []
	last = []

	for each in sent:
		each = each.split()
		try:
			first.append(each[0])
			last.append(each[-1])
		except:
			pass
	print first
	print last


	#print first

	#print last
	

	
	#return text.lower().split()

	





''' These functions will build the chain ''' 
def buildChain(firstOrder, secondOrder):
	firstWord = "it"
	secondWord = "is"
	newT = firstWord + " " + secondWord

	for i in xrange(50):
		try:
			newD = merge(firstOrder,  secondOrder,firstWord, secondWord)
			firstWord = secondWord
			secondWord = getNextWord(newD)
			newT += " " + secondWord
		except:
			break
		#print secondWord

	print newT

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
	''' This will merge the dictionaries of the specific words'''
	list1 = firstOrder[word1]
	list2 = secondOrder[word2]
	newD = dict()
	mergeLists(newD, list1, list2)
	return newD



def mergeLists(newD, list1, list2):
	''' create a new dictionary of frequencies based of two inputs ''' 
	for each in list1:
		if each in list2:
			newD[each] = list1[each]*list2[each]
			
	
''' These functions will build the dictionary '''

def makeDicts(firstOrder, secondOrder, text):
	fillDicts(firstOrder, secondOrder, text)
	toFreqDict(firstOrder)
	toFreqDict(secondOrder)

def add(chainDict, word1, word2):
	if word1 not in chainDict.keys():
		chainDict[word1] = list()
	chainDict[word1].append(word2)
def toFreqDict(fDict):
	for each in fDict:
		tmpL = fDict[each]
		fDict[each] = {x:tmpL.count(x) for x in tmpL}
def fillDicts(firstOrder, secondOrder, text):
	for i in xrange(len(text)-1):
		add(firstOrder, text[i], text[i+1])
		if i != len(text)-2:
			add(secondOrder, text[i], text[i+2])

		#d1 = dict()
		#print type(firstOrder)
		#print type(firstOrder["taylor"])
		#for eachK, eachV in zip(firstOrder.keys(), firstOrder.values()):
		#	firstOrder[eachK] = {x:eachV.count(x) for x in eachV}

	

def test(firstOrder, secondOrder):
	first = "taylor"
	second = "series"




if __name__ == '__main__':
    main() 



