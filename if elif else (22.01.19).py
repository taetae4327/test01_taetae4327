#if를 사용하여 조건이 일치하면 다음 내용을 실행
#조건이 일치하지 않으면 아무 실행 없음

num = 1
if num > 0:
    print('0보다 크다')
elif num == 0: #elif를 사용하여 조건을 추가적으로 검사
              # if나 상위 elif에서 조건이 일치하는 경우가 있으면 하위에 있는 elif와 else는 모두 무시
              #else와 elif는 선택적으로 사용 가능 
    print('0이랑 같다')
else: #else를 뒤에 붙일 경우 if 조건 외에 해당하면 else를 사용하여 프로그램의 흐름을 제어함
    print('0보다 작다')
