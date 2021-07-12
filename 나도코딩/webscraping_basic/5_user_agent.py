# https://www.whatismybrowser.com/detect/what-is-my-user-agent
import requests
url = "https://nadocoding.tistory.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("nadocoding.html", "w", encoding="utf8") as f: #mygoogle.html파일 만들기, 쓰기, 인코딩는 utf8
    f.write(res.text)