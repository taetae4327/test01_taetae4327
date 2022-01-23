def solution(array, commands):
    answer = []
    for com in commands:
        answer.append(sorted(array[com[0]-1:com[1]])[com[2]-1])
    return answer

a = [1, 5, 2, 6, 3, 7, 4] 
c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
result = solution(a,c)
print(result)

