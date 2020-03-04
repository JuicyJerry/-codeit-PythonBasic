# 영어 강사 Coy가 학생들의 영어 단어 암기를 위해 단어장 프로그램을 만들려고 합니다. 이 프로그램은 콘솔로 영어 단어와 한국어 뜻을 받고, vocabulary.txt라는 새로운 텍스트 파일에 단어와 뜻을 정리합니다.
# 프로그램을 실행하면 영어 단어와 한국어 뜻을 입력할 수 있습니다. 단어-뜻을 입력할 때마다 vocabulary.txt에 단어가 정리됩니다.
# 프로그램을 끝내려면, 알파벳 q를 입력하면 됩니다.
# 알파벳 q를 입력함으로써 프로그램을 종료하면 vocabulary.txt에 다음과 같이 단어들이 정리되어 있어야 합니다.
dic = open("vocabulary.txt", "w", encoding="utf-8")

for words in range(10):
    English = input("영어 단어를 입력하세요: ")
    Korean = input("한국어 뜻을 입력하세요: ")
    if English == "q" or Korean == "q" :
        break
    dic.write(English + ": " + Korean + "\n")


dic.close()

while True:
    # 영어 단어 입력
    English= input("영어 단어를 입력하세요: ")
    # q 입력 시 끝
    if English == "q":
        break
    # 한국어 단어 입력
    Korean= input("영어 단어를 입력하세요: ")
    # q 입력 시 끝
    if Korean == "q":
        break
    dic.write("%s: %s\n" % (English, Korean))


dic.close()

# q입력시 바로 종류 시키려면 if문을 사용하는 것보다 while True를 사용하는 것이 확실하다.
# https://blog.naver.com/solleil7829/30019504739
