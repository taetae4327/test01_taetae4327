def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    return int("".join(n))
a=('19305013')
result = solution(a)
print(result)
