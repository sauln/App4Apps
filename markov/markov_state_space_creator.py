# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 18:40:53 2015

@author: nathaniel





attempting to rewrite the markov chain



"""


class markov_state_space():
    def __init__(self, category):
        
        self.category = category
        
        print "set up Text"
        text = self.setupText(category)
        
        print "strip erroneous characters"
        text_2 = self.strip_all(text)
        
        print "gather first words of sentences"
        self.first_words = self.gather_firsts(text_2)
        #print self.first_words        
         
        print self.first_words
       # print text_2
        
        
        
        
        print "generate first and second order dictionaries"
        self.first_order, self.second_order  = self.make_dictionaries(text_2)
        
        
        
        
        
        
        
        
        
        
        
        
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
        # we want to remove things like "key features" and references to the app names
        print "NOT YET IMPLEMENTED: remove all the erroneous characters"
        text_2 = text.replace('\n','.').replace('\x80\x9d', ' ').replace(
                        '\xe2\x80\xa2', ' ').replace('\xe2\x80\x9c', ' ').replace(
                        '\xe2\x97\x8f', ' ').replace('\xe2',' ').replace('"9', ' ').replace(
                        '\x98\x85',' ').replace('"' ,' ').replace('\x80', ' ').replace(
                        '\x99', ' ').replace('(',' ').replace(')', ' ').replace(
                        '..', '.').replace('...', '.')
                        
        text_2 = text_2.lower()

        return text_2




    def gather_firsts(self, text):
        first_words = []
        #split by sentences
        sentences = text.lower().split('.')
        
    
        sentences = [each for each in sentences if each]
        #print sentences       
        
        
        for each in sentences:
            each = each.split()
            try:
                first_words.append(each[0])
            except:
                pass
        
        first_words = self.toFreqList(first_words)
        #print firstLetters
        return first_words
        
        
        
        
    def make_dictionaries(self, text):
        
        
        
        
        
        print "this is the hard part"
        first_order = dict()
        second_order = dict()
        
        
        print "fill dictionaries"        
        #print text
        self.fillDicts(first_order, second_order, text)
        #print first_order
        #print second_order        
        
        self.toFreqDict(first_order)
        self.toFreqDict(second_order)
               
        
    
        
        return first_order, second_order
        
        
    def toFreqList(self, fList):
        fList = {x:fList.count(x) for x in fList}
        return fList  


    def toFreqDict(self, fDict):
        for each in fDict:
            tmpL = fDict[each]
            fDict[each] = self.toFreqList(tmpL)
      

    def fillDicts(self, firstOrder, secondOrder, text):
                
        print "fillDicts"
        text = text.replace('.', ' ').split()
        
        
        
        for i in xrange(len(text)-1):
            self.add(firstOrder, text[i], text[i+1])
            
            if i != len(text)-2:
                self.add(secondOrder, text[i], text[i+2])
                
                

    def add(self, chainDict, word1, word2):
        if word1 not in chainDict.keys():
            chainDict[word1] = list()
            chainDict[word1].append(word2)
        else:
            chainDict[word1].append(word2)


        





