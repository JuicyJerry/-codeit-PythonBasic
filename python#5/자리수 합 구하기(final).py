def sum_digit(num):
    str_num = str(num)
    sum = 0

    # 각 자리수를 sum digit에 추가
    for digit in str_num:
        sum = sum + int(digit)
    # return sum # 이것이 없어서, #22 TypeError: unsupported operand type(s) for +: 'int' and 'NoneType' 발생함.
    return sum


# 1~1000까지 합 구하기
ret = 0
for n in range(1, 1001):
    ret = ret + sum_digit(n) # 함수 내에 에러 발생해도 #15에서 error가 있다고 호출됨
print(ret)

# sum_digit(1001)

