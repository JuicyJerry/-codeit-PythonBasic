# split 메소드는 파라미터로 넘겨주는 값을 기준으로 문자열을 분리시키고, 분리된 값들이 정리되어 있는
# 리스트를 리턴해줍니다.
# split 메소드의 파라미터는 옵셔널 파라미터입니다. 아무 값도 넘겨주지 않았을 경우 기본값으로 ""가 넘어가게
# 됩니다. 그러면 공백(white space)을 기준으로 문자열을 나누게 되는거죠. # 화이트스페이스는 띄어쓰기 + 탭 + 엔터 모두 포함


numbers = "1. 2. 3. 4. 5. 6"
print(numbers.split("."))

numbers = "1. 2. 3. 4. 5. 6"
print(numbers.split(". "))

numbers = "1, 2, 3, 4, 5, 6"
print(numbers.split(","))

full_name = "Kim, Yuna"
print(full_name.split(","))

full_name = "Kim, Yuna"
name_data = full_name.split(", ")

last_name = name_data[0]
first_name = name_data[1]

print(last_name, first_name)

numbers = "1. 2. 3. 4. 5. 6"
number_data = numbers.split(". ")
print(number_data)

print(number_data[0] + number_data[1])
print(int(number_data[0]) + int(number_data[1]))

some_string = "         abc      def  \n gh       ijk lnkdm q   d  r \n s "
print(some_string.split())
