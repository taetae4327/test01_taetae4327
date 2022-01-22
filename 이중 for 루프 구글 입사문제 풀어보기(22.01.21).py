count = 0 #count변수 기본값 0 
for i in range(1,10001): #1부터 10000까지 반복
    for j in str(i): #i를 문자열로 변환 
        if j =='8':
            count += 1 #j에 8이 있으면 count변수에 + 1
print(count)
        
