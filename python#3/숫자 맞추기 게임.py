# 1과 20 사이의 숫자를 맞추는 게임을 만드려고 합니다.
# 앞서 배운 randint 함수와, input 함수의 개념을 활용하여 직접 프로그램을 만들어보세요.

# 진행 방식
# 프로그램을 실행하면 "기회가 *번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: "가 출력됩니다. 총 4번의 기회가 주어지며,
# 사용자가 한 번 추측할 때마다 남은 기회 횟수가 줄어듭니다.
# 정답을 맞추면, "축하합니다. *번만에 숫자를 맞추셨습니다."가 출력되고 프로그램은 종료됩니다.
# 사용자가 입력한 수가 정답보다 작을 경우 "Up"이 출력되고, 입력한 수가 정답보다 클 경우 "Down"이 출력됩니다.
# 정답이 틀렸으면 (1)번부터 다시 진행합니다. 만약 4번의 기회를 모두 사용했는데도 답을 맞추지 못했으면, "아쉽습니다.
# 정답은 *였습니다."가 출력되고 프로그램은 종료됩니다.

#난수
from random import randint
answer = randint(1,20)

trial = 1
guess = int(input("몇 번의 기회를 원하십니까? "))

#while 무한 루프
while True:
    quiz = int(input("기회가 %s번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % (guess) ))
    if quiz == answer:
        break
    elif quiz < answer:
        print("Up")
        trial = trial + 1
        guess = guess - 1
    elif quiz > answer:
        print("Down")
        trial = trial + 1
        guess = guess - 1
    if guess == 0:
#        print("아쉽습니다. 정답은 " + quiz + "였습니다.")
        print("아쉽습니다. 정답은 %s 였습니다." % answer)
        break

# 평가 출력
if quiz == answer:
    print("축하합니다. %s번만에 숫자를 맞추셨습니다." % (trial))
