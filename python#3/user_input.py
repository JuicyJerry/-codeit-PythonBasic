# user에게 어떤 설명할 때 많이 사용됨
name = input("이름을 입력하세요.")
print("Hello " + name)

x = input("숫자를 입력하세요: ")
print(type(x))

# input 함수를 사용하면 무조건 문자열로 받는다.
# 그렇다면 문자열로 받고 싶지 않을 경우는?
x = int(input("첫 번째 정수: "))
y = int(input("두 번째 정수: "))
print("두 정수의 합: %d" % (x + y))
print(type(y))



