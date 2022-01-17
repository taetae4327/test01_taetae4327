#set 중복된 요소가 없는 정령되지 않은 집합
#기본적으로 멤버를 검사하고 중복 항목을 제거
#중괄호나 set()함수를 이용하셔 set생성
market = {'고기','야채','햄','젤리','과자'}
print(market)
print('고기' in market)#있으니 true
print('생선' in market)#없으니 false

a=set('1234567')
b=set('4567890')
print(a)
print(b)
print(a-b)# a와 b집합의 차집합
print(a|b)#a와 b의 합집합 
print(a&b)#a와 b의 교집합 
print(a^b)#a와 b의 합집합에서 교집합을 제외한 집합 
