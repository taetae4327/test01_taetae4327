 # 파일 다루기 - (읽기에는 'r',쓰기에는 'w')

#파일 쓰기(write의 w 사용) 
f = open("파일명",'w')
f.write("data33\n")
f.close()

#파일 추가 쓰기(add의 a 사용)  
f=open("파일명",'a')
f.write("안녕하세요\n")
f.close()


 #파일 읽기(read의 r 사용)
f = open("파일명",'r')
print(f.read())
f.close


#바이너리 파일 읽기 한글이 깨져서 나올때는 data.decord('cp949')입력
f=open("파일명",'rb')#바이너리를 읽도록r 에 b추가
data=f.read()
print(data)
f.close()


'''
#with를 사용한 파일 읽기 쓰기
with open("파일명",'w') as f:
    f.write("test1234")#with를 쓰면 close를 입력하지 않아도 자동으로 닫힘 
with open("파일명",'r') as f:
    print(f.read())
'''
#*상대경로와 절대 경로

#절대경로:처음부터 모든 경로의 이름이 적혀있는 경로
#리눅스는 / 로 시작-/etc/passwd
#윈도우는<알파벳>:/로 시작-C:/Windows/notepad.exe

#상대경로:실행중인 프로그램 위치에서 바라보는 상대적인 위치
#현재 경로- ./
#상위 경로- ../
#파일명만 있는경우-"파일명"
#./파일명-현재 경로에 있는 파일명
#../-상위 경로에 있는 파일명
#../../../../ 파일명-상위 경로의 상위경로의 상위 경로의 상위 경로에 있는 파일명























