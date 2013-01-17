# coding=UTF-8

import re
import urllib




#�ffnet die die URL, liest sie, und speichert sie unter "webpage"
#encode in UTF-8, wegen den doitschen sonderzeichen
url = u"http://www.spiegel.de/"
webpage = urllib.urlopen(url.encode("utf-8")).read()


#such nach den �berschriften der einzelnen Artikel, such nach dem (__),
#das zwischen den strings "title..." und "..>" ist
patFinderTitle = re.compile("title=\"(.*)\">")
#gleiche mit den Links
patFinderLink = re.compile("<a\shref=\"(.*)\" \s title=")

#findall eine RE -> sucht nach ALLEN oben definierten 
#Titeln/Links in der webpage
findPatTitle = re.findall(patFinderTitle, webpage)
findPatLink = re.findall(patFinderLink, webpage)

#erstellt eine (leere) liste in der die Informationen abgespeichert werdne sollen
listiterator = []
#liste wird in der gr��e beschr�nkt, mind. 3, h�chstens 15 links/titel
listiterator = range(2, 17)

#druckt jeweils Titel,Link aus und trennt mit einer leerzeile
for i in listiterator:
	print findPatTitle[i]
	print findPatLink[i]
	print "\n"

