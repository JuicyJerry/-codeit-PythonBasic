numbers = [2, 4, 6, 8, 10, 12, 14]
temp2 = []
i = len(numbers)
# print(int(i), el)
# 리스트 뒤집기
for el in range(len(numbers)):
    temp = (i) - (el + 1)
    temp1 = (numbers[temp])
    temp2.append(temp1)
print("뒤집어진 리스트: " + str(temp2))

