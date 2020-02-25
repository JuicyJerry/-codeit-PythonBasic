## 테스트용 온도 리스트
sample_temperature_list = [40, 15, 32, 64, -4, 11]
sample_temperature_list1 = []

# 화씨 온도 출력
def celsius_to_fahrenheit(sample_temperature_list):
    print("화씨 온도 리스트: " + str(sample_temperature_list))

# 섭씨 온도 출력
def fahrenheit_to_celsius(fahrenheit): # 화씨 온도에서 섭씨 온도로 바꿔주는 함수
    i = 0
    global sample_temperature_list1
    while i < len(fahrenheit):
        n = round(((fahrenheit[i]-32) * 5 / 9), 2)
        s = str(n)
        q = s.split()
        i += 1
        a = sample_temperature_list1 = sample_temperature_list1[0:5] + q[0:5]
        b = str(a)
    print("섭씨 온도 리스트: " + b)

celsius_to_fahrenheit(sample_temperature_list)
fahrenheit_to_celius(sample_temperature_list)
s
