# 이상한 수학 문제1
# while문과 if문을 활용하여 100이하의 자연수 중 8의 배수이지만, 12의 배수는 아닌 것을 모두 출력하세요. 실행하면 아래의 내용이 콘솔에
# 출력되어야 합니다.
i = 0

while i <= 0:
    i = i + 8
    if i % 12 == 0:
        i += 0
    elif i % 8 == 0:
        while i < 10000:
            i += i
        print(i)
    else:
        i += 0


