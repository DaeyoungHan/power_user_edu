# 2022.10 HDY
# 파워유저교육(파이썬) - Part3. 랜덤하면서 중복되지 않은 숫자 뽑기

import random

lotto = random.sample(range(1, 45), 6)
print("로또번호: {}".format(lotto))