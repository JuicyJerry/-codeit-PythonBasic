# 숫자 야구 테스트 페이지
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
print("")
print("세 수를 하나씩 차례대로 입력하세요.")

# 사용자값 입력
i = 0
numbers_box = []
computer_value = []   

def user_list(i):
    while i < 3:
        i = i + 1
        user_value = int(input("%d번째 수를 입력하세요: " % i))
        numbers_box.append(user_value)
    if i > 1:
        del numbers_box[i]
        i = i -1
    print("User Value는 %s 입니다." % numbers_box)

# 랜덤값
    from random import randint
    j = 0
    while j < 3:
        j = j + 1
        computer_value.append(randint(0, 9))

    print("Computer Value는 %s 입니다." % computer_value)

user_list(i)
