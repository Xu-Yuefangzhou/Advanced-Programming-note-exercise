# -*- coding: utf-8 -*-
"""
Created on Tue Apr 4 10:04:29 2018
@author: DELL
"""

__author__ = 'Jane_Xu'
# -*- coding: utf-8 -*-
"""
@author: Jane Xu
"""


from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import word_tokenize as wt #word_tokenize方法
#from nltk.tokenize import regexp_tokenize as rt #用正则表达式方法得出的结果不一样
from nltk import Text
from nltk import FreqDist

corpus_root=''
files = PlaintextCorpusReader(corpus_root, '.*\.txt')
files.fileids()
words=wt(files.raw(fileids=files.fileids()))
#words=rt(files.raw(fileids=files.fileids()),"[\w']+") #正则表达式方法
cps1=Text(words)

fdist1=FreqDist(cps1)
wordlist=fdist1.items()
wordlist_sorted_desc=sorted(wordlist,key=lambda w:w[1],reverse=True)
wordlist_sorted_asc=sorted(wordlist,key=lambda w:w[1])


n=0
m=0

print ("Top 10:")
for word in wordlist_sorted_desc[0:10]:       
    print (word)


print ("\nLast 10:")
for word in wordlist_sorted_asc[0:10]:
    print (word)
