# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup

songs = []

for i in range(4500, 4515):
    result = requests.get("http://www.christianstudy.com/data/hymns/text/c" + str(i) + ".html")
    result.encoding = "big5"

    soup = BeautifulSoup(result.text, "html.parser")
    sel = soup.select("p font")

    song = []
    for s in sel:
        song.append(s.text)
    songs.append(song)

    print(str(i) + " - finished!")

print(songs)