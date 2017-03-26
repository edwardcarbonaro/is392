# Edward Carbonaro
# Web Crawler
# IS 392 Spring 2017


import queue
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError


seedUrlList = ['https://en.wikipedia.org/wiki/Marine_mammal','https://en.wikipedia.org/wiki/Aquatic_mammal']
relatedTermList = ['manatee','sea lion','fur seals','walrus','whales','dolphin','porpoise','sea otter','dugong','polar bear']
q = queue.Queue()
visitedUrlList = []
crawledPageCounter = 0
urlList = []
validator = 'en.wikipedia.org/'



for seedUrl in seedUrlList:
    q.put(seedUrl)    

while (not q.empty() and crawledPageCounter < 500):
    try:
        url = q.get()   
        if url not in visitedUrlList:
            text =""
            html = urlopen(url).read()
            soup = BeautifulSoup(html, "html.parser")
            for paragraph in soup.find_all("p"):
                text += paragraph.text
            visitedUrlList.append(url)
            relatedTermCounter = 0                 
            for relatedTerm in relatedTermList:
                if relatedTerm.lower() in text:
                    relatedTermCounter += 1
            if relatedTermCounter >=2:
                file = open(str(crawledPageCounter)+".html", 'w+')
                file.write(str(text.encode("utf-8")))
                file.close()
                crawledPageCounter += 1

                for link in soup.find_all('a'):
                    urlList.append(("https://en.wikipedia.org"+str(link.get('href'))))

                for url in urlList:
                    if validator in str(url):
                        q.put(url)
    except (HTTPError, URLError):
        continue

file = open("visitedUrlList.txt",'w')
for i in visitedUrlList:
    file.write(i+"\n")
file.close()

        
         






