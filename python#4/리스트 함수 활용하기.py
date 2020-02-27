# 빈 리스트 만들기
numbers = []
i = 0
j = 0
s = 0
q = 0

# numbers에 자연수 1부터 10까지 추가
while i < 10:
    i = i + 1
    numbers.append(i)

print(numbers)

# numbers에서 홀수 제거
while j < len(numbers):
    if numbers[j] % 2 == 0:
        numbers.append(j)
        j = j + 1
    elif numbers[j] % 2 != 0:
        del numbers[j]
        j = j + 1

print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
print(sorted(numbers))


# 이건 왜 안 될까?
#while s < len(numbers):
#    if numbers[s] == 0:
#        numbers.append(s)
#        s = s + 1
#    elif numbers[s] == 0:
#        numbers.insert(s, 20)
#        s = s + 1
#
#print(numbers)
