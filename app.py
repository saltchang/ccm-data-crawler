# -*- coding: UTF-8 -*-

import requests, json, re
from bs4 import BeautifulSoup

start = 4800
end = start + 51

songs = []
outFileURL = "results.json"
outFile = open(outFileURL, "w")

processCounter = 1
ran = end - start

print()
for i in range(start, end):
    try:
        result = requests.get("http://www.christianstudy.com/data/hymns/text/c" + str(i) + ".html")
        result.encoding = "big5"

        soup = BeautifulSoup(result.text, "html.parser")
        sel = soup.select("p font")
        pick = soup.select("p")

        song = {"id_": "",
                "title": "",
                "lyrics": [],
                "album": "",
                "lyricist": "",
                "composer": "",
                "translator": ""
        }
        ss = []
        for s in sel:
            ss.append(s.text.split("\n\r\n"))
        
        song["id_"] = str(i)
        song["title"] = ss[0][0].replace("【","").replace("】","")

        for part in ss[1]:
            part = part.splitlines()
            p = ["p"]
            for line in part:
                if line != "":
                    line = line.replace(" ", "").replace("　", "")
                    p.append(line)
            song["lyrics"].append(p)

        head_ = str(pick[0]).splitlines()[1].replace("</p>", "").replace("\x02", "").replace(" ", "")
        print("\"" + head_ + "\"")
        head = re.split(u"\u3000" + "|<br/>" + "|；" + "|／", head_)
        print(head)
        
        for h in head:
            if h.find("詩集：") != -1:
                song["album"] = h.replace("詩集：", "")
            elif h.find("曲、詞：") != -1 or h.find("詞、曲：") != -1 or h.find("詞曲：") != -1 or h.find("曲詞：") != -1 or h.find("曲/詞：") != -1 or h.find("詞/曲：") != -1:
                h = h.replace("曲、詞：", "").replace("詞、曲：", "").replace("曲詞：", "").replace("詞曲：", "").replace("曲/詞：", "").replace("詞/曲：", "")
                song["lyricist"] = h
                song["composer"] = h
            elif h.find("中譯詞：") != -1 or h.find("譯詞：") != -1 or h.find("譯：") != -1 or h.find("譯者：") != -1 or h.find("中譯：") != -1:
                h = h.replace("中譯詞：", "").replace("譯詞：", "").replace("中譯：", "").replace("譯者：", "").replace("譯：", "")
                song["translator"] = h
            elif h.find("詞：") != -1 or h.find("填詞：") != -1 or h.find("作詞：") != -1:
                song["lyricist"] = h.replace("填詞：", "").replace("作詞：", "").replace("詞：", "")
            elif h.find("曲：") != -1 or h.find("作曲：") != -1:
                if h.find("編曲") == -1:
                    song["composer"] = h.replace("作曲：", "").replace("曲：", "")

        header = []

        # print(pick[0].split("<br>").text.splitlines()[1])
        songs.append(song)
        print("編號：" + str(i) + " - 歌曲資料擷取成功")
    except:
        print("編號：" + str(i) + " - 歌曲資料擷取失敗")
    
    f = (processCounter/ran) * 100
    print("( %.2f"% (f) + "% )\n")
    processCounter += 1

outFile.write(json.dumps(songs, ensure_ascii=False))