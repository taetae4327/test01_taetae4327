def solution(n):
    answer = ''
    for i in range(n):
        if (i%2==0):
            answer=answer+"수"
        elif (i%2==1):
            answer=answer+"박"
    return answer
a = 100
result = solution(a)
print (result)
