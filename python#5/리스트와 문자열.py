alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabets_list[0:5])
print(alphabets_list[4:])
print(alphabets_list[:4])

alphabets_string = "ABCDEFGHIJ"
print(alphabets_string[0:5])
print(alphabets_string[4:])
print(alphabets_string[:4])

list1 = [1, 2, 3, 4]
list2 = [5, 6]
list3 = list1 + list2
print(list3)

print(len("Hello, world!"))

numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)

# Mutable vs Immutable : 리스트는 데이터를 바꿀 수 있지만, 문자열은 데이터를 바꿀 수 없다는 것입니다.
# 리스트와 같이 수정 가능한 자료형을 'mutable'한 자료형이라고 부르고, 문자열과 같이 수정 불가능한 자료형을
# 'immutable'한 자료형이라고 부릅니다. 숫자, 불린, 문자열은 모두 immutable한 자료형입니다.

#1 error : 문자열은 바꾸는 것은 안 됨
name = "codeit"
name[0] = "c"
print(name)

#2
name = "code" + "it"
print(name)
