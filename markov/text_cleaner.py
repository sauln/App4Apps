# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 22:16:00 2015

@author: nathaniel
"""

#text processing script

category = "business"

f_cat = "corpus_" + category + ".txt"



try:
    f = open('../../home/saulgill/saulgill-site/corpus/'+ f_cat, 'r')
except:
    f = open('../corpus/' + f_cat, 'r')
    pass
	
text = f.read()


print text
text_2 = text.replace('\n','.').replace('\x80\x9d', ' ').replace(
                '\xe2\x80\xa2', ' ').replace('\xe2\x80\x9c', ' ').replace(
                '\xe2\x97\x8f', ' ').replace('\xe2',' ').replace('"9', ' ').replace(
                '\x98\x85',' ').replace('"' ,' ').replace('\x80', ' ').replace(
                '\x99', ' ').replace('(',' ').replace(')', ' ').replace(
                '...', '.').replace('.', '').replace(':','').replace('->','').replace(
                '2','').replace('3','').replace('iiix','').lower()
                
#print text_2


