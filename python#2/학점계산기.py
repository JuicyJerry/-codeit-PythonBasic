# 학점 계산기
# 절대 평가 방식으로 총 점수가 90점 이상이면 A를, 80점 이상 90점 미만이며 B를, 70점 이상 80점 미만이며 C를, 60점 이상 70점 미만이면 D를, 60점 미만이며 F를 부과하는 수업입니다.
#예시 : You get a B.
# midterm = 40, final = 45, total = midterm + final


midterm = 40
final = 45
total = midterm + final

if total >= 90:
    print("You get a A.")
elif total >= 80:
    print("You get a B")
elif total >= 70:
    print("You get a C")
elif total >= 60:
    print("You get a D")
else:
    print("You get a F")
