#while 루프 연습문제
#무한 에코 프로그램 작성하기
#일반적인 문자열을 입력하면 입력한 내용을 세번 연속 반복
#help를 입력하면 에코를 해주는 프로그랩입니다 출력
#quit을 입력하면 정말 종료하시겠습니까(Y/N) 출력
#위 질문에서 Y를 누르면 종료 N을 누르면 계속 실행
while(True):
    input1 = input('> ') 
    if input1=='help':
        print("에코를 해주는 프로그램입니다.")
        continue
    elif input1 == 'quit':
        input2 = input('정말 종료하시겠습니까?(Y/N)')
        if input2 == 'Y':
            print('종료합니다')
            break
        elif input2 == 'N':
            print('종료를 취소합니다')
            continue
        else:
            del(input2)
            print('Y와N중 하나를 입력해 주세요')
            input2 = input('정말 종료하시겠습니까?(Y/N)')
            if input2 == 'Y':
                print('종료합니다')
                break
            elif input2 == 'N':
                print('종료를 취소합니다')
                continue   
    else:
        input1 = input1 + ' '
    print (input1 * 3)
    
    
