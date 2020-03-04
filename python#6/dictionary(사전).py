# 사전(dictionary)
# key - value
dic1 = {}
print(dic1)
print(type(dic1))

dic1[5] = 25
dic1[2] = 4
dic1[3] = 9

print(dic1)
print(dic1[3])

# list 순번 개념이 있지만 dic 순번 개념도 없고 정수 이외의 값도 추가할 수 있다.
# 사전이 리스트와 가장 다른 점은 key가 정수뿐만 아니라 아무 자료형이나 될 수 있다는 것입니다
family = {}

family['mom'] = 'grace'
family['dad'] = 'chris'

print(family)
# print(family('dad'))
print(family['dad'])
print(family.keys()) # key들만 모두 받으려면 keys 메소드 사용
print('son' in family.keys()) # 어떤 key가 있는지 확인하려면 이렇게!

# 사전 활용법
# family의 key들을 리스트로 쓰고 싶으면 list 함수로 형 변환을 하면 됩니다.
family_keys = list(family.keys())
print(family_keys)
print(type(family_keys))

# value들을 모두 받기 위해서 values 메소드를 사용합니다.
print(family.values())

# value가 있는지 확인
print('grace' in family.values())

# vaule를 list로 쓰고 싶으면 list함수로 형변환
family_values = list(family.values())
print(family_values)
print(type(family_values))
