print("Hello\n")
print("Hello")

# strip 메소드는 문자열의 가장 앞쪽과 뒤쪽에 있는 화이트 스페이스(white space)가 제거된
#새로운 문자열을 리턴해줍니다. 화이트 스페이스는 그냥 띄어쓰기(" ")뿐만 아니라 탭("\t")과
# 엔터("\n")까지 포괄적으로 얘기하는 것 하지만 strip은 문자열의 가장 앞쪽과 뒤쪽에 있는 화이트 스페이스만
# 제거하지, 중간 중간에 있는 화이트 스페이스는 그대로 둔다는 것을 기억합시다.
print("                    abc   def         ".strip())
print("          \n    abc  def   \n\n         ")
print("          \n    abc  def   \n\n         ".strip())
# 6, print 함수에 \n이 내장되어 있다고 보면 이해가 편하다.
# 기본적으로 print 함수에는 한 줄 띄워주는 기능이 있다.
# 만약 그 값을 제어하고 싶다면 print(", end=")와 같이 end라는 parameter에 특정 값을 넣어 주세요.
# 기본적으로 end='\n'입니다.
