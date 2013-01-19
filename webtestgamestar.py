# coding=UTF-8

import re
import urllib




#öffnet die die URL, liest sie, und speichert sie unter "webpage"
#encode in UTF-8, wegen den doitschen sonderzeichen
url = u"http://www.gamestar.de/index.cfm?pid=945"
webpage = urllib.urlopen(url.encode("utf-8")).read()


#Titel des Spiels
patFinderTitle = re.compile("class=\"linkProductM teaserTextTitle\" href=\".*\">(.*)</a>")

#genre des Spiels
patFinderGenre = re.compile("genre-\d{1,3}.html\">(.*)</a>")
#Alterfreigabe
patFinderAlter = re.compile("USK:</span> (.*)")
#link zur spezifischen Gameseite
patFinderLink = re.compile("linkProductM teaserTextTitle\" href=\"(.*)\">")

#findall eine RE -> sucht nach ALLEN oben definierten 
#Titeln/Links in der webpage
findPatTitle = re.findall(patFinderTitle, webpage)
findPatGenre = re.findall(patFinderGenre, webpage)
findPatAlter = re.findall(patFinderAlter, webpage)
findPatLink  = re.findall(patFinderLink, webpage)




# --------------- Test-Artikel des jeweiligen Spieles öffnen, und den Link zur Wertung finden
#link suchen
"""
patFinderLink = re.compile("href=\"(.*)\">.*</a>")

findPatLink = re.findall(patFinderLink, webpage)

linkiterator = []
linkiterator[:] = range(0, 20)

for i in linkiterator:
	#urlToArticle = "http://www.gamestar.de" , patFinderLink
	#spielwebpage = urllib.urlopen(urlToArticle.encode("utf-8")).read()
	
	print patFinderLink
	
"""






#erstellt eine (leere) liste in der die Informationen abgespeichert werdne sollen
listiterator = []
#liste wird in der größe beschränkt, mind. 3, höchstens 15 links/titel
listiterator[:] = range(0, 88)


#druckt jeweils Titel,Link aus und trennt mit einer leerzeile

for i in listiterator:
	print "Titel:  ",findPatTitle[i]
	print "Genre:  ",findPatGenre[i]
	print "USK:    ",findPatAlter[i]
	
	
	
	#erste Teil der URL, weil im Quelltest nur der /dsad.html teil steht
	urlgamestar = "http://www.gamestar.de"
	#Zusammensetzen in (s)tring form zu einer vollständigen URL
	urlToArticle = "%s%s" % (urlgamestar, findPatLink[i])
	#URL öffnen, utf-8, lesen
	gamePage = urllib.urlopen(urlToArticle.encode("utf-8")).read()
 #Prozentwertung, 01-99, daher \d{2}
	patFinderWertung1 = re.compile("<a href=.*title=\"zur Wertung von.*\">(\d{2})</a>")
# Wertung "Gut", "Sehr Gut" etc., unterschiedliche Anzahl von Zeichen, auch mögl. Sonderzeichen	
	patFinderWertung2 = re.compile("<span class=\"productRatingText\">(.*)</span>")
	
	findPatWertung1  = re.findall(patFinderWertung1, gamePage)
	findPatWertung2  = re.findall(patFinderWertung2, gamePage)
	
	
#nicht alle Spiele wurden getestet und haben eine Wertung, deshalb if/else	
	if(findPatWertung1):
		print "Wertung:  %s  %s" % (findPatWertung1, findPatWertung2)
	
	else:
		print "         Keine Wertung gefunden."
		
	print "\n"