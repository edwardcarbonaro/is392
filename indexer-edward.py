# Edward Carbonaro
# Indexer - Assignemnt 3
# IS 392 Spring 2017


import queue
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
from stop_words import get_stop_words
import glob

n = 0
stop_words = get_stop_words('en')
documents = glob.glob("*.html")
C = {}
T = []



for file in documents:
    n += 1
    f = open(file,'r')
    for line in f:
        T = line.lower().split()

    #Remove words with numbers or symbols in them
    newT = T[:]
    for word in T:
        if word in stop_words:
            newT.remove(word)   
        elif (not word.isalpha()):    
            newT.remove(word)

    #Populates the dictionary
    for t in newT:        
        if t not in C:
            C[t] = [n]
        else:
            C[t].append(n)

    print(n)
    f.close()

#Write the index to file
file2 = open("invertedIndex.txt",'w')
for i in C.items():
    file2.write(str(i) + '\n')
file2.close()


#Write unique terms to file
file3 = open("uniqueTerms.txt",'w')
for i in C.keys():
    if len(C[i]) < 2:
        file3.write(str(i) + '\n')
file3.close()
        



        
         






