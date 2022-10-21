# 2022.10 HDY
# 파워유저교육(파이썬) - 웹스크래핑 예제

# pip install pandas
# pip install lxml
# pip install requests

import requests
import pandas as pd
from datetime import datetime

# 웹 요청시 사용할 헤더, 헤더를 사용하지 않으면 경우에 따라 웹서버에서 정상적이지 않은 접근으로 간주하여 차단될 수 있다
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42'}

# 스크래핑할 대상 웹url
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8%EC%A1%B0%ED%9A%8C"

# url 페이지를 연다
response = requests.get(url=url, headers=header)

# 페이지가 정상적으로 열어졌다면 status_code == 200 으로 응답한다
if response.status_code == 200:
    # reponse.text에는 페이지 소스가 담겨 있다
    html = response.text

    # 환율이 출력되는 테이블을 pandas로 가져옴
    tables = pd.read_html(html)

    # 전체내용 출력
    print(tables)

    # 자료형 출력
    print(type(tables))     # <class 'list'>

    # 리스트의 길이
    print(len(tables))      # 1

    # 리스트 접근
    print(type(tables[0]))  # <class 'pandas.core.frame.DataFrame'>

    # 사용하기 쉽도록 df변수에 tables[0]을 할당
    df = tables[0]

    # dataframe 멤버에 접급
    print(df.loc[0]['매매기준율'])

    # 현재일자 yyyy.mm.dd_HHMMSS
    dt = datetime.now().strftime('%Y.%m.%d_%H%M%S')

    # 엑셀로 저장
    df.to_excel('환율_' + dt + '.xlsx')
else:
    # 웹페이지 응답이 정상적이지 않을경우의 응답 코드 출력
    print(response.status_code)