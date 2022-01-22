#while문은 for문과 같이 일정한 코드를 반복할 때 사용
#사용 형식:while(조건문)
#조건문이 참일 경우에만 구문 실행
'''
for a in range(100):#0부터99까지 리스트 생성
    if a == 10:
        break#만약  a 가 10 이라면 for문 탈출
    print(a)
    continue
    break#위에 countinue가 있으므로 실행 안 됌
'''
'''a=0
while(True):
    if a == 10:
        break
    print(a)
    a += 1
    continue
    break
   ''' 
a=0

while(True):
    a += 1
    if a % 2==0: #만약 a가 짝수라면 
        pass #아무것도 하지 않는다
    else: #짝수가 아니라면
        print(a)#홀수 프린트
        if a > 1000:#a 가 1000 이상이면 멈추기
            break
         
        
