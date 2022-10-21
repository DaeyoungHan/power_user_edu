# 2022.10 HDY
# 파워유저교육(파이썬) - Part3. 랜덤하면서 중복되지 않은 숫자 뽑기

import random   # random 라이브러리를 사용할거야

rnd_num = 0     # 숫자를 하나씩 뽑을텐데, 뽑히는 숫자를 담을곳이 필요해
lotto = []      # 6가지 숫자를 lotto라는곳에 담을래

# 숫자를 6개를 뽑아야하니 6번 반복해줘
for i in range(6):
    while rnd_num in lotto:             # rnd_num이 lotto에 있다면 멈추지 말고 반복해줘
        rnd_num = random.randint(1, 45) #  1 ~ 45 사이의 정수를 하나 뽑아줘
    lotto.append(rnd_num)               # 뽑은 수를 lotto에 추가해줘

lotto.sort()                            # lotto를 정렬해줘
print("로또번호: {}".format(lotto))      # lotto를 출력해줘