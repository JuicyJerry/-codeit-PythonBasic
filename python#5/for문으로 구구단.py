#예전에 했던 구구단 프로그램을 이번에는 while문 대신 for문을 써서 만들어보세요. 아래와 같이 출력되어야 합니다.
for elements in range(9):
    for another_elements in range(9):
        print("%s * %s = %s" % ((elements + 1), (another_elements + 1), ((another_elements + 1) * (elements + 1))))
