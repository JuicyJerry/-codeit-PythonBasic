# data 폴더의 chicken.txt를 읽어 들이고, strip과 split을 써서 12월 코빠닭의 하루 평균 매출을 계산하세요.
# 평균을 구하기 위해서는 총 매출을 총 일수로 나누면 됩니다. 만약 한 달이 28일이거나 30일이면,
# 그에 맞게 평균 매출을 구할 수 있도록 코드를 짜셔야 합니다.

# 정답
sales = open("chicken.txt", "r", encoding="utf-8")
day = 0
sum = 0
for i in sales:
    i_box = i.strip().split(": ")
    package = int(i_box[1])

    sum = sum + package
    day = day + 1

print(sum / day)



# 파일 닫기
sales.close()
