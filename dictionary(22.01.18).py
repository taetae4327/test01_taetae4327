#dictionary
#dict는 딕셔너리의 약자로 값과 속성으로 이루어짐
#값은 문자열 정수 배열 dict등 삽입 가능
#"key"를 사용하여 "value"를 인덱스
#키는 strings나 number가 될 수 있으나,변하지 않아야 함
#키는 고유한 성질을 가져야 함
#정령되지 않은 key:value 쌍
#'{'와'}'를 활용하여 Dictionary를 만들고,그 안에 ':'를 사용하여 key와value를 구분
#key를 사용하여 value를 저장


data = {'강태규':{'영어':100,'수학':90},
        '김철수':{'과학':90,'사회':80}}
print(data)
print(data['강태규']['영어']) 
data['강태규']['영어']=90#영어의 값 변경
print(data['강태규']['영어'])
data['강태규']['과학']=95#data에 새로운 값 추가 
print(data)
print(data['김철수'])
print(data.keys())#data의 keys만 출력
print(data.values())#data의 값만 출력
print(data.items())#data의 모든 keys와 값 출력

