# 학생들이 저번에 만든 단어장 퀴즈 프로그램은 늘 순서가 같아서 재미가 없다고 합니다. 이번에는 randint 함수와 사전(dictionary)을 이용해서 vocabulary.txt의 단어들을 랜덤한 순서로 테스트하는 프로그램을 써보세요.
# 같은 단어를 여러번 물어봐도 괜찮고, 프로그램은 알파벳 q를 입력할 때까지 실행됩니다.

# 파일 읽기
dic = open("vocabulary.txt", "r", encoding="utf-8")
box = []
box1 = []
random_box = []

# 랜덤 번호: 만들기
from random import *
randomNum = randint(1, 11)
random_box.append(randomNum)

# 랜덤 번호: 중복 방지
while randomNum in random_box:
    randomNum = randint(1, 11)
#print(randomNum)
#print(type(randomNum))

# 변수 만들기
for i in dic:
    word = i.strip().split(": ")
    english = word[0]
    korean = word[1]
    #print(korean)
    # txt 파일 밑에서 2줄 이상이 공백이 생기면 IndexError: list index out of range 에러 발생
    #print(korean, english)
    box.append(korean)
    box1.append(english)
#print(box1)
#print(type(word))

# quiz 랜덤으로 발생.
temp_box = []
temp_box1 = []
for x in range(1):
    for y in box[1:randomNum]:
        temp_box = y.split(", ")
    for y in box1[1:randomNum]:
        temp_box1 = y.split(", ")
    #print(x, temp_box[x])
    #print(x, temp_box1[x])

# conditions setting
    while True:
        # quiz(영어) 입력
        question = input("%s: " % temp_box[x])
        # quiz(한국어) 입력
        answer = temp_box1[x]

        if question == "q":
             break
        # 정답
        if question == answer:
            print("맞았습니다!\n")
        # 오답
        if question != answer:
            print("아쉽습니다. 정답은 '%s'입니다." % answer)
        elif question == "q":
            break
# 종료
dic.close()

## => 한 문제 풀고 나서 다른 문제로 넘어가는 부분이 해결되지 않음
# if문은 참이면 elif문 조건이 참인지 거짓인지 판단을 안 합니다. if문이 거짓이면 첫뻔째 elif문 조건을 판단합니다.
# 첫번째 elif문을 판단해서 참이면 두 번째 elif문을 판단 안 하고 거짓이어야 두 번째 elif문을 판단합니다.
