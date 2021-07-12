import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soip객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs) # a element 속성 정보를 출력
# print(soup.a["href"]) # a element의 href 속성 '값' 정보를 출력

# print(soup.find("a",attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 a태그 element를 찾아
# print(soup.find(attrs={"class":"Nbtn_upload"})) #class="Nbtn_upload"인 어떤 element를 찾아줘
# print(soup.find(attrs={"title":"외모지상주의"})) #class="Nbtn_upload"인 어떤 element를 찾아줘
# print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a)