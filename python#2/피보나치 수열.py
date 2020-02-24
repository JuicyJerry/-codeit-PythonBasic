#피보나치 수열이란 첫 번째 항과 두 번째 항이 1이고, 세 번째 항부터는 바로 앞의 두 항의 합으로 정의된 수열입니다.
# 예를 들어서 세 번째 항은 첫 번째 항(1)과 두 번째 항(1)을 더한 2이며, 네 번째 항은 두 번째 항(1)과 세 번째 항(2)을 더한 3이
# 될 것입니다. 이러한 방식으로 피보나치 수열의 첫 10개 항은 1, 1, 2, 3, 5, 8, 13, 21, 34, 55입니다. 피보나치 수열의 첫 20개 항을
# 차례대로 출력하는 프로그램을 써보세요.
# 내가 푼 코드
n = 0
a = 1
b = 1


while n < 20:
    n = n + 1
    sum = a + b
    if n < 3:
        sum = 1
    elif n > 2:
        a = b
        b = sum
    print(sum)

# 정답으로 제시된 코드
# 상수
count = 20

# 변수
current = 1
previous = 0
i = 0

while i < count:
    print(current)

    temp = previous
    previous = current
    current = current + temp

    i = i + 1
