# for 반복문
big_bang = ["지드래곤", "태양", "탑", "대성", "승리"]

#i = 0
#while i < len(big_bang):
#    print(big_bang[i])
#   i = i + 1

# member(for문의 수행부분에서만 쓰이고 사라지는 local변수) 대신 아무 변수명을 지어줘도 가능하다. but, 의미있는 이름을
# 짓는 것을 지향합니다. 이와 같이 프로그래밍 언어에서 동일한 기능을 깔끔하게 만들어 놓은 것을 'Syntactic sugar(꿀)'이라고
#부릅니다.
for member in big_bang:

    print(member)

for num in [1, 3, 5, 7, 9]:
    print(num * num)

# range 함수: 간편함 깔끔함, 메모리 효율성
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)
for i in range(1, 11): # 1~10
    print(i)

for i in range(10): # 0~9
    print(i)

for i in range(3, 17, 3): # 3~ 16까지 간격 3씩
    print(i)

for i in range(3, 16, 3):
    print(i)

for i in range(3, 15, 3):
    print(i)
