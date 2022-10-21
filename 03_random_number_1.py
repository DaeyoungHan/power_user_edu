# 2022.10 HDY
# 파워유저교육(파이썬) - Part3. 랜덤하면서 중복되지 않은 숫자 뽑기

import random

lotto = []
rnd_num = random.randint(1, 45)

for i in range(6):
    while rnd_num in lotto:
        rnd_num = random.randint(1, 45)
    lotto.append(rnd_num)

lotto.sort()
print("로또번호: {}".format(lotto))