# 2의 n제곱의 결과값을 출력하는 프로그램을 만드세요. 아래와 같이 2^0 = 1부터 2^10 = 1024까지 출력되어야 합니다.
for elements in range(11):
    print("%s^%s = %s" % (2, elements, 2 ** elements))
