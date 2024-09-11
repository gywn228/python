# [1] 파일 쓰기(생성)
open('test1.txt' , 'w') #
open('../test2' , 'w') #


# [2] 파일의 내용 쓰기
file4 = open('./test4.txt', 'w') # 쓰기 모드 파일 생성 하고 파일 객체로 반환 받아서 변수에 저장
file4.write("python")
file4.close()

file5 = open('./test5.txt' , 'w' , encoding='utf-8')
for value in range(1 , 11) :
    # range (시작값 , 끝값) : 시작값 부터 끝값 전까지 1씩 증가 하는 리스트 반환
    data = f'{value}번째 줄 입니다 \n'
    file5.write(data)
file5.close() # 파일 닫기

# [3] 키보드로 부터 입력 받은 값을 파일에(file6.txt)에 저장
uzer = input("입력 : ")
file6 = open('./test6.txt' , 'w' , encoding= 'utf-8')
file6.write(uzer)
file6.close()

# [4] 파일을 읽는 여러가지 방법
file = open('./test5.txt' , 'r' , encoding= 'utf-8')
# 1. .readline() # 파일 내 한줄 씩 읽어 오는 함수
line = file.readline()
print(line)
while True : # 무한 반복문
    line = file.readline() 
    if not line : # 만약에 읽어온 문자가 ' ' 공백 이면
        break # 가장 가까운 반복문을 종료
    print(line)
file.close() # 파일 닫기

# 2. .readlines() # 파일 내 한줄 씩 요소로 해서 여러줄을 리스트로 반환 함수
file = open('./test5.txt' , 'r' , encoding='utf-8')
lines = file.readlines()
print(lines)
for line in lines : # for 반복변수 in 리스트 : 리스트 내 요소 하나씩 반복변수에 대입 반복
    print(lines)
file.close()
# 3. .read() # 파일 내 모든 내용을 문자열로 읽어 오는 함수
file = open('./test5.txt' , 'r' , encoding= 'utf-8')
content = file.read()
print(content)
file.close()

# [5] 키보드로 부터 입력 받은 값이 저장된 (file6.txt) 파일을 읽어 오기
uzer2 = input('입력 : ')
file = open('./test6.txt' , 'w' , encoding='utf-8')
file.write(uzer2)
file = open('./test6.txt' , 'r' , encoding='utf-8')
read = file.read()
print(read)
file.close()

# 파일 처리 와 예외 처리 같이 작성 하기
    # 1. 파일 명의 오타 있거나 존재 하지 않는 파일은 예외 발생 # FileNotFoundError
try:
    file = open('./test7.txt' , 'r' , encoding='utf-8')
except FileNotFoundError as e : # 2. 예외 발생 할 경우 안내 문구
    print('존재 하지 않는 파일 이거나 경로에 문제가 있습니다.')
