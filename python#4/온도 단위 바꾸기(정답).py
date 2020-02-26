def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

sample_temperature_list = [40, 15, 32, 64, -4, 11]

print("화씨 온도 리스트: " + str(sample_temperature_list))


i = 0
while i < len(sample_temperature_list):
    sample_temperature_list[i] = round(fahrenheit_to_celsius(sample_temperature_list[i]), 2)
    i += 1
print("섭씨 온도 리스트: " + str(sample_temperature_list))

# fahrenheit_to_celsius(sample_temperature_list) # 이거 뭐지..? #16가 문제였구만.
# sample_temperature_list[0] = fahrenheit_to_celsius(sample_temperature_list[0])
# sample_temperature_list[0] = int(fahrenheit_to_celsius(sample_temperature_list[0]))
# sample_temperature_list[0] = round(fahrenheit_to_celsius(sample_temperature_list[0]))
