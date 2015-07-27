<<<<<<< HEAD
def setupText(category):
	feedstock = readFile(category)
	first = getFirstWords(feedstock)
	text = feedstock.lower().split()
	return first, text
=======
>>>>>>> origin/markov-revamp






<<<<<<< HEAD
def generate():
    firstOrder = dict()
    secondOrder = dict()
    first, text = setupText(category)
    first = makeDicts(firstOrder, secondOrder, text, first)
    #return buildChain(firstOrder, secondOrder,first)
=======
>>>>>>> origin/markov-revamp






<<<<<<< HEAD
def readFile(category):
	#try:
	#	f = open('corpus/corpus.txt', 'r')
	#except:
	try:
		f = open('../../home/saulgill/saulgill-site/corpus/corpus_' + category + '.txt', 'r')
	except:
		f = open('corpus/corpus_' + category + '.txt', 'r')
		pass
	
	txt = f.read()
	return txt
=======
>>>>>>> origin/markov-revamp


class transition_dictionary():
    
    
    def __init__(self, category):
    	print "set up Text"
    	self.first, text = self.setupText(category)
    		
    	print "create dictionaries"
    	self.firstOrder = dict()
    	self.secondOrder = dict()
    
    	#first = self.makeDicts(self.firstOrder, self.secondOrder, text, first)
    	print "finished"
        


    def setupText(self, category):
    	feedstock = self.readFile(category)
    	first = self.getFirstWords(feedstock)
    	text = feedstock.lower().split()
    	return first, text

    def makeDicts(self, firstOrder, secondOrder, text, first):
    	fillDicts(firstOrder, secondOrder, text)
    	toFreqDict(firstOrder)
    	toFreqDict(secondOrder)
    	first = self.toFreqList(first)
    	return first


    def readFile(self, category):
    	#try:
    	#	f = open('corpus/corpus.txt', 'r')
    	#except:
    	
    	f_cat = "corpus_" + category + ".txt"
    	try:
    		f = open('../../home/saulgill/saulgill-site/corpus/'+ f_cat, 'r')
    	except:
    		f = open('../corpus/' + f_cat, 'r')
    		pass
    	
    	txt = f.read()
    	return txt
    




    def getFirstWords(self, txt):
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
        
    
    def generate(self):
        firstOrder = dict()
        secondOrder = dict()
        first, text = setupText()
        first = makeDicts(firstOrder, secondOrder, text, first)
        #return buildChain(firstOrder, secondOrder,first)
    

    
    def fillDicts(self, firstOrder, secondOrder, text):
    	for i in xrange(len(text)-1):
    		add(firstOrder, text[i], text[i+1])
    		if i != len(text)-2:
    			add(secondOrder, text[i], text[i+2])
    
    def add(self, chainDict, word1, word2):
    	if word1 not in chainDict.keys():
    		chainDict[word1] = list()
    	chainDict[word1].append(word2)

    def toFreqDict(self, fDict):
    	for each in fDict:
    		tmpL = fDict[each]
    		fDict[each] = toFreqList(tmpL)
    
    def toFreqList(self, fList):
    	fList = {x:fList.count(x) for x in fList}
    	return fList
    

def go(category):
    print "set up Text"
    first, text = setupText(category)


    print "create dictionaries"
    firstOrder = dict()
    secondOrder = dict()

    first = makeDicts(firstOrder, secondOrder, text, first)
    print "finished"
    return firstOrder, secondOrder, first

