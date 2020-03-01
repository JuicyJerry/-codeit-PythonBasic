# 피타고라스 수란 피타고라스의 정리(a^2 + b^2 = c^2)를 만족하는 세 자연수 쌍 (a, b, c) 입니다.
# 예를 들어, 3^2 + 4^2 = 5^2이기 때문에 (3, 4, 5)는 피타고라스 수입니다.
# a < b < c일때, a + b + c = 1000을 만족하는 피타고라스 수 (a, b, c)는 단 하나입니다. 이 경우, a * b * c는 얼마인가요?
#1
for number in range(1, 500):
    a = number
    aa = number*number
    for another_number in range(1, 500):
        b = another_number
        bb = another_number*another_number
        for new_another_number in range(1, 500):
            c = new_another_number
            cc = new_another_number*new_another_number
            if a < b < c and (aa + bb) / 2 == cc / 2 and a + b + c == 1000:
                print(a, b, c)
                print(a*b*c)
                break
#2
for a in range(1, 500):
    for b in range(1, 500):
        for c in range(1, 500):
            d = (c*c / 2)
            e = ((a*a) + (b*b) / 2)
            if a < b < c and d == e and a + b + c == 1000:
                print(a, b, c)
                print(a*b*c)
                break


#200 375 425
