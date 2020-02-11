# _*_ coding: utf-8 _*_
#   assignment operator: 지정연산자

name = "이정환"
x = 1
x = x + 1

#   함수의 실행 순서 : 함수 호출 순서
def hello():
    print("Hello")
    print("Wwlcome to Codeit")


print("함수 호출 전")
hello()
print("함수 호출 후")

def square(x):
    return x * x


print("함수 호출 전")
print(square(3) + square(4))
print("함수 호출 후")
print()

# return문 제대로 이해하기 : (함수가) 무언가를 돌려주는 것
# return문의 역할: 값 돌려주기, 함수 종료시키는 역할
def square(x):
    print("함수 시작")
    return x * x
    print("함수 끝") # dead code


print(square(3))
print("hello")
print()


# return과 print의 차이
def print_square(x):
    print(x * x)

def get_square(x):
    return x * x

print_square(3)
get_square(3)
print()

def print_square(x):
    print(x * x)

def get_square(x):
    return x * x

print(print_square(3))


# 옵셔널 파라미터 : 파라미터의 기본값을 설정해두면 함수 호출을 할 때 파라미터에 해당되는 값을 넘겨주지 않을 경우, 그 파라미터는 기본값을 갖게 됩니다.


def myself(name, age, nationality = "한국"):
    print("내 이름은 %s" % name)
    print("내 나이는 %d살" % age)
    print("국적은 %s" % nationality)


myself("코드잇", 1)
myself("코드잇", 1, "미국")

# optional parameter : 모두 마지막에 있어야 함
# def myself(name, nationality = "한국", age):
#     print("내 이름은 %s" % name)
#     print("내 나이는 %d살" % age)
#     print("국적은 %s" % nationality)
#
#
# myself("코드잇", 1)
# myself("코드잇", "미국", 1)
#



# Syntactic Sugar: 아래와 같이 자주 쓰이는 표현을 간략하게 쓸 수 있게 해 주는 문법을 말함.
x += 1
x *= 2
x -= 3
x /= 4
x %= 5

#scope: 변수가 사용 가능한 범위
# 파라미터도 로컬 변수!
# 함수에서 변수를 사용하면, 로컬 변수를 먼저 찾고 나서 글로벌 변수를 찾음

def my_function():
    x = 3   #지역 변수 : 로컬 변수
    print(x)


my_function()
print(x)

x = 3 # 전역 변수 : 글로벌 변수
def my_function():
    print(x)


my_function()
print(x)

# 상수 : 프로그램 내내 바뀌지 않는 값, 대문자로 써주는 것이 파이썬 커뮤니티의 규칙임.
# 상수를 절대로 바꾸면 안 됨
