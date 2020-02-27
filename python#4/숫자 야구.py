# The Game of Number Baseball
print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
print("세 수를 하나씩 차례대로 입력하세요.")

# conditions
def entry():
    print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
    print("세 수를 하나씩 차례대로 입력하세요.")

from random import randint
answer = randint(0, 9)
i = 0
number = []
while i < 3:
    i = i + 1
    guess = int(input("%s번째 수를 입력하세요 " % i))
    print(guess)
    if guess > 0 and guess < 10 and guess not in number and guess < 0 or guess > 9:

        print(number)
        print(guess)

        i = i + 1
        print(number)
        print(guess)

# In seraching of existing number(s)
def in_list(number, answer):
    j = 0
    while j < len(number):
        if number[j] == answer:
            print(answer)
            return True
        j = j + 1

    print(answer)
    return False

print(in_list(number, answer))
if in_list(number, answer) == False:
    print(entry)
elif in_list(number,answer) == True:
    print("")

