#튜플은 리스트와 다르게 서로 다른 형식의 데이터를 집합으로 생성 가능
tuple1 = 12234, 5678,'abcd','efgh'
print(tuple1)
#튜플의 요소는 변조 삭제 불가
#새로운 값을 넣으려 하면 오류구문 출력
#가변하는 list는 포함가능
tuple2 = [1,2,3],'a'
print(tuple2)
tuple2[0].append(4)
print(tuple2)
