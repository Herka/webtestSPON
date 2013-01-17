import urllib #from bs4 import BeautifulSoup
import re

#copy alle of the content form the provided web page
#webpage = urllib.urlopen("http://feed.huffingtonpost.com/huffingtonpost/LatestNews").read()
webpage = urllib.urlopen("http://feeds.huffingtonpost.com/huffingtonpost/LatestNews").read()
#grab everything that lies between the titl tags using a REGEX

patFinderTitle = re.compile("<title>(.*)</title>")

#grab the link to the original article using a REGEX
patFinderLink = re.compile("<link .* href=\"(.*)\" />")

#Store all of the titles and links found in 2lists
findPatTitle = re.findall(patFinderTitle, webpage)
findPatLink = re.findall(patFinderLink, webpage)

#create an iterator that will cycle through the first 16 articles and skip a few
listiterator = []
listiterator = range(2, 150)

#print out the result to the screen
for i in listiterator:
	print findPatTitle[i] #the title
	print findPatLink[i] #the link to the original article
	print "\n"
	

#articlePage = urlopen(findPatLink[i].read() #Grab all of the content from the original article
