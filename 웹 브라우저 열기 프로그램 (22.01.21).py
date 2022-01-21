import webbrowser#파이선 프로그램 불러오기(웹브라우저를 여는 프로그램)
import time#파이선 프로그램 불러오기(프로그램에 시간차를 둘 수 있게 해주는 프로그램) 
weplist=["https://www.youtube.com/"]#weplist란 리스트 만들기

for i in range(10): #10 번 반복하기
    for url in weplist:    #리스트:weplist에 있는 url열기 
        webbrowser.open(url) 
        time.sleep(2)


