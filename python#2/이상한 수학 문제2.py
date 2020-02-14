# 이상한 수학 문제2
# 10보다 작은 2 또는 3의 배수는 2, 3, 4, 6, 8, 9이며, 이들의 합은 32입니다.
# while문과 if문을 활용하여, 1000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력하는 프로그램을 써보세요.
# console: 333167

#1
i = 0
j = 0

while i <= 0 or j <= 0:
    i = i + 2
    j = j + 3
    if i % 2 or j % 3:
        i += 0
        j += 0
    elif i + j == 32:
        while :



i = 0
j = 0

while i < 10:
    i = i + 1
    j = j + 1
    if i % 2 == 0 or j % 3 == 0
        print(i, j)



#2

i = 0
j = 0

while i < 10 and j < 10:
    i = i + 2
    #j = j + 3
    if i % 6 == 0:
        i += 2
        #print(i, j, "!")
    elif j % 3 == 0 and i < 10:
        #print(i, j, "!!")
        while i < 32:
            i = i + i
            #j = j + j
        print(i, j)

#3
i = 0
j = 0

while i <= 0:
	i = i + 2
    j = j + 3
   	if i % 2 == 0 or i % 3 == 0:
        print(i, j)
        while i < 1000 and j < 1000:
            print(i, j)
            i += i
            j += j
            print(i, j)
        	sum = i + j
        print(sum)
        print(i, j)


#4

i = 0
sum = 0

while i <= 1000:
    sum = sum + i
    i = i + 1
    print(sum, i, "!")
    if i % 2 == 0:
        i += 0
    elif sum % 3 == 0 and sum <= 333167:
    	print(sum)
