def adder(a,b): #함수 만들기
    if a > b: a,b=b,a
    return sum(range(a,b+1))#sum함수 사용
print(adder(3,5))
