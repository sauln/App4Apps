def setupText():
	feedstock = readFile()
	first = getFirstWords(feedstock)
	text = feedstock.lower().split()
	return first, text


def getFirstWords(txt):
	firstLetters = []
	#split by sentences
	sent = txt.lower().split('.')

	#add just the first words of each sentence
	for each in sent:
		each = each.split()
		try:
			firstLetters.append(each[0])
		except:
			pass

	return firstLetters 


def generate():
    firstOrder = dict()
    secondOrder = dict()
    first, text = setupText()
    first = makeDicts(firstOrder, secondOrder, text, first)
    #return buildChain(firstOrder, secondOrder,first)

def makeDicts(firstOrder, secondOrder, text, first):
	fillDicts(firstOrder, secondOrder, text)
	toFreqDict(firstOrder)
	toFreqDict(secondOrder)
	first = toFreqList(first)
	return first

def fillDicts(firstOrder, secondOrder, text):
	for i in xrange(len(text)-1):
		add(firstOrder, text[i], text[i+1])
		if i != len(text)-2:
			add(secondOrder, text[i], text[i+2])
			
def add(chainDict, word1, word2):
	if word1 not in chainDict.keys():
		chainDict[word1] = list()
	chainDict[word1].append(word2)
	
def toFreqDict(fDict):
	for each in fDict:
		tmpL = fDict[each]
		fDict[each] = toFreqList(tmpL)
	
def toFreqList(fList):
	fList = {x:fList.count(x) for x in fList}
	return fList

def readFile():
	f = open('corpus.txt', 'r')
	txt = f.read()
	return txt


	
	
	
	
	
print "set up Text"
first, text = setupText()


print "create dictionaries"
firstOrder = dict()
secondOrder = dict()
		
first = makeDicts(firstOrder, secondOrder, text, first)
print "finished"
