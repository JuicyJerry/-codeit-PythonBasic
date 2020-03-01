# 파라미터로 정수형 num의 값을 받는 sum_digit 함수를 쓰세요. sum_digit은 num의 각 자리수를 더한 값을 리턴해주는 역할을 합니다.
# 예를 들어 12의 각 자리수는 1, 2이므로 sum_digit(12)는 3(1 + 2)을 리턴해줍니다.
# 마찬가지로 486의 각 자리수는 4, 8, 6이므로 sum_digit(486)은 18(4 + 8 + 6)을 리턴해줍니다.
# for문을 사용하여, sum_digit(1)부터 sum_digit(1000)까지의 합을 구해보세요.

def sum_digit(num):
    for num in range(1, num+1):
        if num > 0 and num < 10:
            num = list(str(num))
            plus = int(num[0])
            combination = plus * (int(num[0]))
            # combination = combination + combination
            #print(plus)
            #print(num)
            print(combination)
            #print("")
        elif num > 9 and num < 100:
            num = list(str(num))
            plus = int(num[0]) + int(num[1])
            combination = plus * (int(num[0]) + int(num[1]))
            # combination = combination + combination
            #print(plus)
            #print(num)
            print(combination)
            #print("")
        elif num > 99 and num < 1000:
            num = list(str(num))
            plus = int(num[0]) + int(num[1]) + int(num[2])
            combination = plus * (int(num[0]) + int(num[1]) + int(num[2]))
            # combination = combination + combination
            #print(plus)
            #print(num)
            print(combination)
            #print("")
        elif num > 999 and num < 10000:
            num = list(str(num))
            plus = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])
            combination = plus * (int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]))
            # combination = combination + combination
            #print(plus)
            #print(num)
            print(combination)
            #print("")
        else:
            print("조건에 부합하지 않는 수입니다.")

sum_digit(1000)
