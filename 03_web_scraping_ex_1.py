# 2022.10 HDY
# 파워유저교육(파이썬) - 웹스크래핑 예제

# pip install beautifulsoup4
# pip install requests

import requests
from bs4 import BeautifulSoup

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42'}
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%8B%AC%EB%9F%AC%EC%9B%90%ED%99%94%ED%99%98%EC%9C%A8"

response = requests.get(url=url, headers=header)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    currency_tag = soup.select_one('#_cs_foreigninfo > div > div.api_cs_wrap > div > div.c_rate > div > div.rate_compare > div.compare_area > div > div:nth-child(3) > div.input_box._input_box > span.recite._recite.result')

    print(currency_tag)
    print(currency_tag.getText())
else:
    print(response.status_code)


# 연습: 네이버에서 주가 가져오기