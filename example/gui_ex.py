# 2022.10 HDY
# 파워유저교육(파이썬) - GUI 프로그램 예제

# pip install tk

import tkinter          # tkinter 모듈 사용

window = tkinter.Tk()   # 윈도우 객체를 생성

window.title("나의 첫번째 GUI 프로그램")        # 윈도우 타이틀바 제목
window.geometry("640x400+100+100")            # 640x400 크기의 창을 생성해서 100, 100에 위치
window.resizable(False, False)                # 창 크기조절 불가

count = 0               # 카운트를 위한 전역변수

def countUP():          # 카운트 함수
    global count        # count는 전역변수를 사용
    count += 1          # 1 증가
    label_count.config(text=str(count))     # label_count의 text를 count로 설정

label = tkinter.Label(window, text="Hello World") # label을 생성하여 text는 Hello World로 지정, 부모창은 window
label.pack()                                    # window에 위치

label_count = tkinter.Label(window, text="0")   # label_count를 생성하여 text는 0로 지정, 부모창은 window
label_count.pack()                              # window에 위치

button = tkinter.Button(window, overrelief="solid", text="Count", width=15, command=countUP, repeatdelay=1000, repeatinterval=100)  # 버튼생성
button.pack()   # window에 위치

window.mainloop()   # window를 띄운다