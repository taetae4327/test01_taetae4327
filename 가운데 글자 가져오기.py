def solution(s):
    answer = ''
    a = len(s)
    if a % 2 == 0 :
        a = (a-2) / 2
    else :
        a = (a-1) / 2
    return s[int(a) : -int(a)]
print(solution("taetae"))
