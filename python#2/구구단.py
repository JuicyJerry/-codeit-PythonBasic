 # 구구단을 만들어보세요. while문을 사용하여 콘솔에 아래 문장들이 출력되게 프로그램을 작성하세요.
 # 1단부터 9단까지

dan = 0
while dan < 9:
    dan = dan + 1
    num = 0
    while num < 9:
        num = num + 1
        print(f"{dan} * {num} = {dan * num}")

