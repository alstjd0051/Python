from bs4 import BeautifulSoup

import csv
import re
import requests

# 1. csv file open
csv_name = "main_all.csv"
csv_open = open(csv_name, "w+", encoding="utf-8")
csv_writer = csv.writer(csv_open)
csv_writer.writerow(("drink", "image_url"))

# 2.BeautifulSoup
crawling_url = "https://www.starbucks.co.kr/menu/drink_list.do"
response = requests.get(crawling_url)

# 3. Parsing html code
html = response.text
bs = BeautifulSoup(response.text, 'html.parser')

# 4. Get element selector
lists = bs.select(
    "#container > div.content > div.product_result_wrap.product_result_wrap01 > div > dl > dd:nth-child(2) > div.product_list > dl > dd:nth-child(2) > ul > li:nth-child(1) > dl > dd")
imgs = bs.select("#container > div.content > div.product_result_wrap.product_result_wrap01 > div > dl > dd:nth-child(2) > div.product_list > dl > dd:nth-child(2) > ul > li:nth-child(1) > dl > dt > a > img") 24
# 5. Save drink, img
with open(csv_name, "w+", encoding="utf-8") as file:
    for i in range(len(lists)):
        # drink
        drink = lists[i]['dd']

        # image_url
        img_url = crawling_url + '/' + imgs[i]['src']

        writer = csv.writer(file)
        writer.writerow((drink, img_url))
