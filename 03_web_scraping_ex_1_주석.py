# 2022.10 HDY
# 파워유저교육(파이썬) - 웹스크래핑 예제

# pip install beautifulsoup4
# pip install requests

import requests
from bs4 import BeautifulSoup

# 웹 요청시 사용할 헤더, 헤더를 사용하지 않으면 경우에 따라 웹서버에서 정상적이지 않은 접근으로 간주하여 차단될 수 있다
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42'}

# 스크래핑할 대상 웹url
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%8B%AC%EB%9F%AC%EC%9B%90%ED%99%94%ED%99%98%EC%9C%A8"

# url 페이지를 연다
response = requests.get(url=url, headers=header)

# 페이지가 정상적으로 열어졌다면 status_code == 200 으로 응답한다
if response.status_code == 200:
    # reponse.text에는 페이지 소스가 담겨 있다
    html = response.text

    # 페이지 소스를 bs4에서 해석(파싱)할 수 있도록 변환
    soup = BeautifulSoup(html, 'html.parser')

    # 환율이 출력되는 태그를 가져옴
    currency_tag = soup.select_one('#_cs_foreigninfo > div > div.api_cs_wrap > div > div.c_rate > div > div.rate_compare > div.compare_area > div > div:nth-child(3) > div.input_box._input_box > span.recite._recite.result')
    
    # 가져온 태그 출력
    print(currency_tag)             # <span class="recite _recite result">1,433.90 원</span>

    # 태그의 텍스트만 출력
    print(currency_tag.getText())   # 1,433.90 원
else:
    # 웹페이지 응답이 정상적이지 않을경우의 응답 코드 출력
    print(response.status_code)