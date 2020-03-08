from random import randint

# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
# get user numbers and computer numbers
number_box = []
user_box = []
def generate_numbers(num):
    # user numbers
    while len(user_box) < (num):
        new_user_box = randint(1, 45)
        while new_user_box in user_box:
            new_user_box = randint(1, 45)
        user_box.append(new_user_box)

    # computer numbers
    # preservation of duplicate
    while len(number_box) < (num):
        new_number_box = randint(1, 45)
        while new_number_box in number_box:
            new_number_box = randint(1, 45)
        number_box.append(new_number_box)

    return number_box, user_box


generate_numbers(6)

# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
bonus_user_box = []
bonus_computer_box = []

ordered_user_box = sorted(user_box)
ordered_number_box = sorted(number_box)
def draw_winning_numbers(bonus):
    print("%s, user lotto number" % ordered_user_box)
    print("%s, computer lotto number" % ordered_number_box)

    while len(bonus_user_box) < bonus:
        another_user_box = randint(1, 45)
        bonus_user_box.append(another_user_box)
    print("%s, user bonus lotto number" % bonus_user_box)

    while len(bonus_computer_box) < bonus:
        another_number_box = randint(1, 45)
        bonus_computer_box.append(another_number_box)
    print("%s, computer bonus lotto number" % bonus_computer_box)


    #print("%s, %s" % (bonus_user_box, bonus_computer_box))

    return ordered_user_box, ordered_number_box

draw_winning_numbers(1)


length_count = 0
length_count_box = []
bonus_num_check = (bonus_user_box == bonus_computer_box)
# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):

    length_count = 0
    for elements in list1:
        for another_elements in list2:
            if elements == another_elements:
                length_count = length_count + 1

    length_count_box.append(length_count)

    #print(length_count)
    #print("!%s 입니다." % length_count_box)


    return length_count, bonus_num_check


count_matching_numbers(ordered_user_box, ordered_number_box)


# 로또 등수 확인하기
def check(numbers, winning_numbers):

    #print("!!%s 입니다." % numbers)
    #print(bonus_num_check)

    if numbers == [6]:
        return 1000000000   # 10억
    elif numbers == [5] and winning_numbers:
        return 50000000  # 5천만원
    elif numbers == [5]:
        return 1000000  # 1백만원
    elif numbers == [4]:
        return 50000    # 5만원
    elif numbers == [3]:
        return(5000) # 5천원
    else:
        return ("꽝")

print(check(length_count_box, bonus_num_check))
