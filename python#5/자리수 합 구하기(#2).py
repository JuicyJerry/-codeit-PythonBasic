# 파라미터로 정수형 num의 값을 받는 sum_digit 함수를 쓰세요. sum_digit은 num의 각 자리수를 더한 값을 리턴해주는 역할을 합니다.
# 예를 들어 12의 각 자리수는 1, 2이므로 sum_digit(12)는 3(1 + 2)을 리턴해줍니다.
# 마찬가지로 486의 각 자리수는 4, 8, 6이므로 sum_digit(486)은 18(4 + 8 + 6)을 리턴해줍니다.
# for문을 사용하여, sum_digit(1)부터 sum_digit(1000)까지의 합을 구해보세요.

def sum_digit(num):
    for a in range(1, 10): # 1의 자리
        for b in range(0, 10): # 10의 자리
             for c in range(0, 10): # 100의 자리
                 for d in range(0, 2): # 1000의 자리
                    e = a + b + c + d
                    num = (e * ((d * 1000) + (c * 100) + (b * 10) + (a * 1)))
    print(num)
sum_digit(1000)
