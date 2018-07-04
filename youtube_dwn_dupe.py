from __future__ import unicode_literals
from bs4 import BeautifulSoup
import urllib2
import os
import youtube_dl
ydl_opts={ }
search = raw_input("What do you want to search?: ")
search2 = search.replace(" ", "+")
url = "https://www.youtube.com/results?search_query=" + search2 + "&page=&utm_source=opensearch"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content,'html.parser')
ze = 0
zl = []
for l in soup.find_all('a'):
    c = l.get('title')
    a = l.get('href')
    b = a[:6]
    
    if (b == "/watch" and c and ze<5):
        print " "
        print ze+1, c
        ze=ze+1
        zl.append(a)

zc = int(raw_input("Pick one: "))
page = "youtube.com/" + zl[zc-1]
command = "youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 " + str(page)
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([page])
print "Done!"


