# 2022.10 HDY
# 파워유저교육(파이썬) - Part3. 랜덤하면서 중복되지 않은 숫자 뽑기

import random   # random 라이브러리를 사용할거야

lotto = random.sample(range(1, 45), 6)  # 1 ~ 45 사이의 숫자중에서, 6개의 중복되지 않은 숫자를, 샘플링해줘
print("로또번호: {}".format(lotto))      # lotto를 출력해줘