# 파라미터로 정수형 num의 값을 받는 sum_digit 함수를 쓰세요. sum_digit은 num의 각 자리수를 더한 값을 리턴해주는 역할을 합니다.
# 예를 들어 12의 각 자리수는 1, 2이므로 sum_digit(12)는 3(1 + 2)을 리턴해줍니다.
# 마찬가지로 486의 각 자리수는 4, 8, 6이므로 sum_digit(486)은 18(4 + 8 + 6)을 리턴해줍니다.
# for문을 사용하여, sum_digit(1)부터 sum_digit(1000)까지의 합을 구해보세요.

def sum_digit(num):
    for a in range(1, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0,2):
                    e = d + c + b + a
                    num = (e * ((d * 1000) + (c * 100) + (b * 10) + (a * 1)))
                    if 0 < num < 10:
                        a = 0
                        b = 0
                        c = 0
                        d = 0
                        num = (e * ((d * 1000) + (c * 100) + (b * 10) + (a * 1)))
                    elif 9 < num < 100:

                        c = 0
                        d = 0
                        num = (e * ((d * 1000) + (c * 100) + (b * 10) + (a * 1)))
                    elif 99 < num < 1000:
                        d = 0
                        num = (e * ((d * 1000) + (c * 100) + (b * 10) + (a * 1)))
                    elif 999 < num < 10000:
                        num = (e * ((d * 1000) + (c * 100) + (b * 10) + (a * 1)))
    print(num)
sum_digit(1000)

