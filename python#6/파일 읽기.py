f = open('chicken.txt', 'r', encoding = 'utf-8') # 한 번에 읽어주기 때문에 파일이 큰 경우 메모리 문제가 발생할 수 있음
# print(f.read()) # 파일을 읽기 위해서는 open 내장 함수를 쓰면 된다.

in_file = open('chicken.txt', 'r', encoding='utf-8') # r: read, w: write, 같은 폴더에 넣어주어야 인식됨

# print(type(in_file))

for line in in_file: # 문자열 리스트(list of strings)처럼 다룰 수 있다.
    print(line.strip())

in_file.close() # 파일을 열면 프로그램이 실행되는 동안 메모리를 차지하고 있는데,
# close 메소드를 쓰면 메모리를 해방시켜 줄 수 있다. 데이터가 큰 파일일 경우 꺼두질 않으면 메모리 낭비가 됨

