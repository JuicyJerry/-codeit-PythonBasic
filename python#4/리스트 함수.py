# len함수: 리스트 안의 원소 개수를 세즈는 역할을 합니다.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(len(numbers))

# 원소 추가하기: insert와 append를 사용하여 리스트에 원소를 추가할 수 있습니다.
numbers.append(5)
print(numbers)

numbers.append(9)
print(numbers)

# 원소 빼기: del 함수를 하용함으로써 원하는 리스트의 원소를 삭제할 수 있습니다.
del numbers[3]
print(numbers)

del numbers[0:4]
print(numbers)

numbers.insert(5, 0)
print(numbers)

# sorted 함수: 리스트의 원소들을 오름차순으로 정렬한 새로운 리스트를 리턴해줍니다.
print(sorted(numbers))

# 리스트 연결하기: +를 사용하여 연결할 수 있습니다.
alphabet1 = ["a", "b", "c"]
alphabet2 = ["d", "f", "g"]
alphabet = alphabet1 + alphabet2

print(alphabet)



