# 숫자 야구 테스트 페이지
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
print("")
print("세 수를 하나씩 차례대로 입력하세요.")

# 랜덤값
from random import randint

computer_values = []

# 세 개 뽑을때까지 반복
while len(computer_values) < 3:
    new_computer_values = randint(0, 9)

    # 새로운 수 나올때까지 다시 뽑기
    while new_computer_values in computer_values:
        new_computer_values = randint(0, 9)
    computer_values.append(new_computer_values)

print("Computer Values는 %s 입니다." % computer_values)

# 사용자값 입력
numbers_box = []
count = 0
new_count = 0

while numbers_box != computer_values:
    count = 0
    numbers_box = []
    while len(numbers_box) < 3:
        user_values = int(input("%d번째 수를 입력하세요: " % (int(len(numbers_box)) + 1)))

        # 겹치지 않고 범위에 해당될 때까지 다시 뽑기
        while user_values in numbers_box:
            user_values = int(input("%d번째 수를 입력하세요: " % (int(len(numbers_box)) + 1)))
        #numbers_box.append(user_values)

        while user_values < 0 or user_values > 9:
           user_values = int(input("%d번째 수를 입력하세요: " % (int(len(numbers_box)) + 1)))
        numbers_box.append(user_values)
        print("User Values는 %s 입니다." % numbers_box)

    # strike와 ball 구분
    i = 0
    strike = 0
    ball = 0
    while i < len(numbers_box):
        if numbers_box[i] == computer_values[i]:
            strike = strike + 1
            print("%sstrike "% i)
        elif numbers_box[i] in computer_values:
            ball = ball + 1
            print("%sball" % i)
        i += 1
    print("%dS, %dB" % (strike, ball))
    new_count = new_count + 1
    if strike == 3:
        print("축하합니다. %s번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (new_count ))
        break
