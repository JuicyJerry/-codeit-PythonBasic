# 이제 단어 암기를 위해서 학생들을 퀴즈해주는 프로그램을 만들고 싶습니다. vocabulary.txt의 첫 줄부터, 콘솔에 한국어 뜻을 알려주면 학생이 영어 단어를 입력하는 방식입니다. 맞는 답이 나오면 맞았습니다!가 출력되고 틀린 답이 나오면 아쉽습니다. 정답은 OOO입니다. 형식으로 나옵니다.
dic = open("vocabulary.txt", "r", encoding="utf-8")
box = []
for i in dic:
    box.append(i)
#print(box)
    word = i.strip().split(": ")
    korean = word[0]
    english = word[1]
    #print(word)
    #print(korean, english)
# txt 파일 밑에서 2줄 이상이 공백이 생기면 IndexError: list index out of range 에러 발생
    x = 0
    while True:
        question = input("%s: " % korean)
        answer = english
        if question == answer:
            print("맞았습니다!")
            break
        elif question != answer:
            print("아쉽습니다. 정답은 %s입니다." % answer)
            break
    x = x +1

