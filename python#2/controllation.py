# _*_ coding: utf-8 _*_
#   제어문
#   while 반복문
## while 조건부분: 수행부분  // 조건부분(header): 결과값으로 불린이 나오는 식, 수행부분(body): 반복적으로 실행하고 싶은 명령들
i = 1
while i <= 1:
    print("i can code too!")
    i += 1


# while 반복문 정리
# 이제 반복문을 쓰는 이유를 아시겠나요? 반복문은 귀찮은 작업을 컴퓨터에게 떠넘기기 위한 용도입니다.
# 좋은 소프트웨어 엔지니어가 되려면 게을러져야 합니다.
# 컴퓨터 과학에서 다루는 여러 도구(tool)들을 배워서, 게으른 소프트웨어 엔지니어가 되세요. 어떻게 하면 똑똑한 프로그램을 작성할 수
# 있을지, 효율적(efficient)인 알고리즘을 작성할 수 있을지 끊임없이 고민해보세요.

# 실습과제
# while문을 사용하여 100 이상의 자연수 중 가장 작은 23의 배수를 출력해보세요.
i = 100

while i != 115:
    i = i + 15
    print(i)


# if문
# if 조건부분:
#   수행부분

# 조건부분: 결과값으로 불린이 나오는 식
# 수행부분: 조건부분이 True일 때 실행하고 싶은 명령들

# else:
#     수행부분
# 조건부분: 결과값으로 불린이 나오는 식
# 수행부분: 조건부분이 False일 때 실행하고 싶은 명령들

temperature = 11

if temperature <= 10:
    print("자켓을 입니다.")
else:
    print("자켓을 입지 않는다.")

# while문의 경우 조건부분이 True일 동안에 수행부분이 계속 실행되지만,
# if문은 조건부분이 참일 때 수행부분이 딱 한 번 실행됩니다.
# while문 : 반복문(loop), if문 : 조건문(conditional)이라고 부릅니다.
# if elif else

# 학점 계산기

midterm = 40
final = 45
total = midterm + final

if total >= 90:
    print("You get a A.")
elif total >= 80:
    print("You get a B")
elif total >= 70:
    print("You get a C")
elif total >= 60:
    print("You get a D")
else:
    print("You get a F")

# 이상한 수학 문제1
i = 0

while i < 100:
    i = i * 8
    if i % 12 == 0:
        print(i)
    else :
        print(i)













