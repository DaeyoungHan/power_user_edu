import random # random 모듈을 가져옴

import urllib.request # 파이썬 표준 라이브러리에서 urllib 패키지의 request 모듈 가져오기


# 1~10사이의 랜덤한 정수를 가져온다
n = random.randint(1, 10)
print(n)

# google.com 웹페이지를 연다
response = urllib.request.urlopen('http://www.google.co.kr')
print('응답코드:', response.status)

print('module, package, library') # print는 내장함수