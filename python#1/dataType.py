# _*_ coding: utf-8 _*_

#   나머지
print(7 % 3)

#   거듭제곱
print(2 ** 3)
print(2.0 ** 3.0)
print(2 ** 3.0)

#   나눗셈 : 결과값이 무조건 소수(floating point)으로 나온다고 함 cf) integer:정수
print(7 / 2)
print(6 / 2)
print(7.0 / 2)
print(7.0 / 2.0)
print()

#   floor division (버림 나눗셈)
print(7 // 2)
print(8 // 3)
print(8.0 // 3)
print(8.0 // 3.0)
print(round(3.1415926536, 4)) #    반올림
print()

#   문자열(data type)
print("코드잇")
print("유재석")
print("I'm excited to learn Python!")
print("I\'m \"excited\" to learn Python!")
print("Hello" + "World")
print("3" + "5")

#   형 변환(Type Conversion, Type Casting)
print(int(3.8))
print(float(3))
print(int("2") + int("5"))
print(float("1.1") + float("2.5"))
print(str(2) + str(5))
age = 7
#   print("제 나이는 " + age + " 살입니다.")
print("제 나이는 " + str(age) + " 살입니다.")
# print(int("Hello"))




#   format 메소드를 이용한 문제열 포맷팅
# 오늘은 2020년 02월 11일입니다.
year = 2020
month = 2 # 02 는 decimal integer literals x but, octal integers 가능
day = 10

print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일입니다.")
print("오늘은 {}년 {}월 {}일입니다.".format(year,month,day)) # stir.format()

date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year,month,day))

#   format 메소드 다루기
print("저는 {}, {}, {}를 좋아합니다.".format("박지성", "유재석", "빌게이츠"))
print("저는 {1}, {0}, {2}를 좋아합니다.".format("박지성", "유재석", "빌게이츠"))

num_1 = 1
num_2 = 3.0
print("{0} 나누기 {1}은 {2}입니다.".format(num_1, num_2, num_1 / num_2))
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1 / num_2)) # f : floating, ".2" : 소수점 2번째 자리로 반올림

# data type formating하는 다양한 방식
## 가장 오래된 방식 : 포맷 스트링 (% 기호; %s, %d) c, java
name = "코드잇"
age = 32

print("제 이름은 %s이고 %d살입니다." % (name, age))

## 새로운 방식 (f-string)
name1 = "고드잇"
age1 = 3

print(f"제 이름은 {name1}이고 {age1}살입니다.")


# 불 대수 : 일상적인 논리를 수학적으로 표현한 것, 진리값(참, 거짓) 연산(and, or, not), 명제: 참, 거짓이 확실한 문장
## True and True = True (이외, False)
## True or True = true, False * False = False, 이외 True
## not x = True or False


# 불린형(boolean) : 참과 거짓 구별
print(True and True)
print(True and False)
print(False and False)
print(False and True)
print()

print(True or True)
print(True or False)
print(False or False)
print(False or True)
print()

print(not True)
print(not False)
print()

print(2 > 1)
print(2 < 1)
print(3 >= 2)
print(3 <= 3)
print(2 == 2)
print(2 != 2)

print("Hello" == "Hello")
print("Hello" != "Hello")

print(not not True)
print(not not False)

# type 함수
print(type(3))
print(type(3.0))
print(type("3"))
print(type("True"))
print(type(True))

def hello():
    print("Hello World")

print(type(hello))
print(type(print))
