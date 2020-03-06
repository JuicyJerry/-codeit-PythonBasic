# user numbers
user_number = input("로또 번호 7개를 입력하시요: ")
user_number_box = list(user_number)
while len(user_number_box) < 8:
    if len(user_number_box) == 7:
        print("%s는 로또 개수에 부합합니다." % user_number_box)
        break
    elif len(user_number_box) != 7:
        print("%s는 로또 개수와 부합하지 않습니다. 다시 입력하세요." % user_number_box)


from random import randint
# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기

number_box = []
def generate_numbers(num):
    # preservation of duplicate
    while len(number_box) < (num):
        new_number_box = randint(1, 45)
        while new_number_box in number_box:
            new_number_box = randint(1, 45)
        number_box.append(new_number_box)
    print(number_box)


generate_numbers(6)

# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers(bonus):
    ordered_number_box = sorted(number_box)
    print(ordered_number_box)

    while len(ordered_number_box) < (bonus):
        another_number_box = randint(1, 45)
        while another_number_box in ordered_number_box:
            another_number_box = randint(1, 45)
        ordered_number_box.append(another_number_box)
    print(ordered_number_box)


draw_winning_numbers(7)

