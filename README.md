# Song Crawler

一個很簡單的 Python 爬蟲程式，
從 [武林英雄帖](http://www.christianstudy.com) 網站爬取基督教詩歌的程式。

## 安裝

### 下載檔案

```shell

$ git clone https://github.com/saltchang/song-crawler.git

$ cd songs-crawler
```

### 安裝環境

註：請先在電腦安裝 Python3

建立虛擬環境 venv：

```shell

$ python3 -m venv ./venv

$ source venv/bin/acitvate

$ pip install -r requirements.txt
```

確認所需套件皆已安裝：

```shell

$ pip freeze

beautifulsoup4==4.7.1
certifi==2019.3.9
chardet==3.0.4
Click==7.0
Flask==1.0.2
get==2019.3.22
idna==2.8
itsdangerous==1.1.0
Jinja2==2.10
MarkupSafe==1.1.1
post==2019.3.22
public==2019.3.22
query-string==2019.3.22
requests==2.21.0
soupsieve==1.9
urllib3==1.24.2
Werkzeug==0.15.1
```

## 使用方法

直接在 venv 中執行：

```shell

$ python songs_crawler.py [start] [end]
```

其中：
start 代表開始的歌曲編號，最小 1000
end   代表結束的歌曲編號，最大 5000

爬蟲完畢會將歌曲資料存成 JSON

輸出檔案位於 ```./output/```

## 範例

```shell

$ python songs_crawler.py 4020 4040

[ 4.8% ] 編號：4020 - 歌曲資料擷取成功

[ 9.5% ] 編號：4021 - 歌曲資料擷取成功

[ 14.3% ] 編號：4022 - 歌曲資料擷取成功

...

[ 95.2% ] 編號：4039 - 歌曲資料擷取成功

[ 100.0% ] 編號：4040 - 歌曲資料擷取成功

所有資料已經擷取完畢，JSON檔案儲存於 ./output/c_4020_4040.json
```

如欲快速確認輸出結果：

```shell

cat ./output/c_4020_4040.json


[{"id_": "4020", "title": "美麗的我",

...

"composer": "編曲：區柏冬@音樂私房菜", "translator": ""}]

```
