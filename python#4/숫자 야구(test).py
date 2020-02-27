# 숫자 야구 테스트 페이지
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
print("")
print("세 수를 하나씩 차례대로 입력하세요.")

# 랜덤 값
from random import randint
j = 0
computer_values = []
while j < 3:
    j = j + 1
    computer_values.append(randint(0, 9))

print(computer_values)


# 사용자 값
i = 0
user_values = []
random_values_box = []
while i < 3:
    random_values = int(input("%s번째 수를 입력하세요: " % (i + 1)))
    user_values.append(random_values)
    print(user_values)
    print(random_values_box)

    if user_values[i] < 0 or user_values[i] > 10: # and / or 각각의 결과에 대한 차이는 무엇일까?
        print("범위에 해당되지 않는 수 입니다.")
        del user_values[i]
        #del random_values_box
        #i = i - 1    # continue

    #elif i > 1 and random_values == user_values:
    elif user_values[i] in random_values_box:
        print("중복되는 수 입니다.")
        del user_values[i]
        #i = i - 1    # continue

    #else:
    #    i = i - 1
print(user_values)


# comparison
def in_list(user_values, computer_values):
    q = 0
    matching_number = []
    while q < len(user_values):
        if user_values[q] == computer_values[q]:
            print("ㅇㅇ")


