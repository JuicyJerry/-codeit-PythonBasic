# 10보다 작은 2 또는 3의 배수는 2, 3, 4, 6, 8, 9이며, 이들의 합은 32입니다.
# while문과 if문을 활용하여, 1000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력하는 프로그램을 써보세요.
# console: 333167

i = 1
sum = 0

while i < 1000:
    if i%2==0:
        sum = sum + i
    elif i%3==0:
         sum = sum + i
    i = i + 1 
print(sum)
