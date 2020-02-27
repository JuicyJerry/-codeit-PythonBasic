# 환율에 따라 화폐를 교환해주는 서비스를 운영하고 있습니다. 신속한 환전을 위하여 원(￦) 단위로 정리되어 있는 리스트를 달러($)와
# 엔(￥)으로 변환해주는 프로그램을 써야합니다. # 현재 환율은 1달러 당 1000원, 1000엔 당 8달러입니다. 이 정보를 이용해서
# 파라미터 won으로 한국 금액을 받고 미국 금액을 리턴해주는 krw_to_usd 함수와, 파라미터 dollars로 미국 금액을 받고 일본 금액을
# 리턴해주는 usd_to_jpy 함수를 쓰세요. 그리고 이 함수들을 활용해서 아래에 원(￦)으로 정리된 amounts리스트를 달러($) 리스트와
# 엔(￥) 리스트로 변환 시켜보세요.

i = 0
j = 0
usd = 1
krw = 1
jpy = 1

# 원(￦)에서 달러($)로 바꿔주는 함수
def krw_to_usd(won):
    dollors = won * (1 / 1000)
    return dollors


# 달러($)에서 엔(￥)로 바꿔주는 함수
def usd_to_jpy(dollars):
    yen = dollars * (1 / 8) * 1000
    return yen


# 원(￦)으로 각각 얼마인가요?
amounts = [1000, 2000, 3000, 5000, 8000, 13000, 21000, 34000]
print("한국 화폐: " + str(amounts))


# amounts를 원(￦)에서 달러($)로 바꿔주기
while i < len(amounts):
    amounts[i] = round(krw_to_usd(amounts[i]), 0)
    i = i + 1
print("미국 화폐: " + str(amounts))


# amounts를 달러($)에서 엔(￥)으로 바꿔주기
while j < len(amounts):
    amounts[j] = round(usd_to_jpy(amounts[j]), 2)
    j = j + 1
print("일본 화폐: " + str(amounts))
