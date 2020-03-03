#1
def mask_security_number(security_number):
    # security_number를 리스트로 변환
    num_list = list(security_number)

    # 마지막 네 값을 *로 대체
    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = "*"
        print(num_list)
    # 리스트를 문자열로 복구
    total_str = "".join(num_list)

    return total_str

#2
def mask_security_number(security_number):
    return security_number[:len(security_number) - 4] + "****"


print(mask_security_number("880720-1234567"))
# print(mask_security_number("8807201234567"))
# print(mask_security_number("930124-7654321"))
# print(mask_security_number("9301247654321"))
# print(mask_security_number("761214-2357111"))
# print(mask_security_number("7612142357111"))
