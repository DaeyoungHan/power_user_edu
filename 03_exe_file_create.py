# 2022.10 HDY
# 파워유저교육(파이썬) - Part3. exe 파일 만들기

# pip install pyinstaller

import random
import os

lotto = random.sample(range(1, 45), 6)
print("로또번호: {}".format(lotto))

os.system('pause')

# pyinstaller --clean --onefile 03_exe_file_create.py