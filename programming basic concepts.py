# _*_ coding: utf-8 _*_

#   single line comment
#   주석
print("Hello World") # 이것도 주석

#   프로그래밍의 자료형
print(2+5)
print(2+2.0)
# print(2+"2")
print(3 > 7)
print(7>3)

#   추상화: 복잡한 내용은 숨기고, 주요 기능에만 신경쓰자!
#   변수(variable), 함수(function), 객체(parameter)
x = 254
y = 317
print(x+y)
#    변수(variable) : 값을 저장하는 것
burger_price = 4990
fries_price = 1490
drink_price = 1250

print(burger_price)
print(burger_price * 2)
print(burger_price + fries_price)
print(burger_price * 3 + fries_price * 2 + drink_price)

#   함수(fucntion) : 명령을 저장하는 것
burger_price = 4990
print(burger_price) #   내장함수(ex. print)

def hello(): #  this singline is called by function of header
    print("Hello!")
    print("Welcome to Codeit")

hello()
hello()
hello()

#   파라미터(parameter) : 함수에 넘겨 주는 값

def hello(name): #  name : parameter
    print("Hello!")
    print(name)
    print("Welcome to Codeit!")

hello("Chris")

def print_sum(a, b, c):
    print(a + b + c)

print_sum(7, 3, 10)

#   return statemnet // https://www.codeit.kr/community/threads/2169
#   지정연산자 (y = st 에서 '=')

def get_square(x) :
    return x * x
print(get_square(3))

def get_square1(x):
    return x * x
y = get_square1(3)
print(y)

def get_square2(x):
    return x * x
print(get_square2(3) + get_square2(4))
