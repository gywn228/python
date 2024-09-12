# 문자열
# - 문자열 은 리터럴 # 불면성 (수정 불가능) 특징
from tkinter.font import names

# [1] 파이썬에서 문자열 표현 하는 방법 : 1. "" 2. '' 3. """ 4. '''
a = "코딩도 헤매는 만큼 자기 땅이야"
a = '코딩도 헤매는 만큼 자기 땅이야'
a = """코딩도 헤매는 만큼 자기 땅이야"""
a = '''코딩도 헤매는 만큼 자기 땅이야'''

# [2] 문자열 연산
print('python' + 'is fun') # python is fun
print('=' * 50) # ==================================================
a = 'python'
a+= ' is fun'
print(a) # python is fun

# [3] 문자열 인덱싱 # 문자열 내 문자 위치를 인덱스(번호) 표현 # 리스트/튜플
print('python'[0]) # p # p[0] y[1] t[2] h[3] o[4] n[5]
print('python'[2]) # t
print('python'[4]) # o
print('python'[-1]) # n
print('python'[-3]) # h

# [4] 문자열 슬라이싱 # [시작번호 : 끝번호(미만) : 증강 단위]
print('python'[0 : 2]) # py
print('python'[ : 3]) # pyt
print('python'[2: ]) # thon
print('python'[ : ]) # python
print('python'[2 : -1]) # tho
print('python'[ : : 2]) # pto
print('python'[ : : -1]) # nohtyp # 문자열 역순

# [5] 문자열 관련 함수/기능
    # . (접근/도트) 연산자
a = '코딩도 헤매는 만큼 자기 땅이야.'
# 1. .count('찾을 문자') # 문자열 내 찾을 문자가 존재 하면 개수 반환 함수
print(a.count('자')) # 1 # 문자 열 내 '자' 인 문자가 1개 존재
print(a.count('가')) # 0 # 지정한 문자 열 내 '가' 인 문자가 0개 존재

# 2. .find('찾을 문자') # 문자열 내 찾을 문자가 존재 하면 찾은 문자의 인덱스 반환
print(a.find('자')) # 11 # 문자열 내 '자' 인 문자의 인덱스 위치
print(a.find('가')) # -1 # 문자열 내 '가'인 문자의 인덱스 없다는 뜻

# 3. .index('찾을 문자') # 문자열 내 찾을 문자가 존재 하면 찾은 문자의 인덱스를 없으면 예외 발생 하는 함수
print(a.index('자'))
try:
    print(a.index('가'))
except ValueError as e:
    print(e)

# 4. '특정문자' .join("문자열" 또는 리스트) # 문자열 내 또는 리스트 요소 사이의 특정 문자를 삽입 해서 반환 필수
print(',' .join(a)) # 코,딩,도, ,헤,매,는, ,만,큼, ,자,기, ,땅,이,야,.
b = ['python','java','c','c++']
print(' <=> '.join(b)) # python <=> java <=> c <=> c++

c= 'Abcdef'

# 5. .upper() # 대문자로 치환 해서 반환 함수
print(c.upper()) # ABCDEF
print(c)
c = c.upper()
print(c)

# 6. .lower() # 소문자로 치환 해서 반환 함수
print(c.lower()) # abcdef

# 7. .lstrip() # # 문자열 내 왼쪽 공백 제거 된 문자열 반환 함수
d = '     pyt hon        ' # 앞뒤 공백이 많은 문자열
print(d.lstrip()) # pyt hon

# 8.  .rstrip() # 문자열 내 오른쪽 공백 제거 된 문자열 반환 함수
print(d.rstrip()) #      pyt hon

# 9.  .strip() # 문자열 내 양쪽 공백 제거 된 문자열 반환 함수
print(d.strip()) #      pyt hon
print(d)

# 10. .replace ( '기존문자' '새로운문자') # 문자열 내 기존 문자가 존재 하면 새로운 문자로 치환/변경 해서
print(a.replace("코딩","파이썬")) # 파이썬도 헤매는 만큼 자기 땅이야.

# 11. .split('기존문자') # 문자열 내 기존 문자 기준 으로 문자열을 분해 해서 리스트 반환
print(a.split()) # ['코딩도', '헤매는', '만큼', '자기', '땅이야.']
d = '가:나:다:라'
print(d.split(":")) # ['가', '나', '다', '라']

# 실습1 :
csvdata = """유재석,39\n강호동,45\n신동엽,21"""

str1 = csvdata.split('\n')
print(str1)
for str2 in str1 : # 'str1' 이라는 리스트를 반복문 사용하여 하나씩 반복하기
    # for 반복요소 in 리스트 : 리스트 내 첫번째 요소부터 마지막 요소까지 반복요소에 대입 반복
    str3 = str2.split(',')
    print(f'{str3[0]} \t {str3[1]}')

# 실습2 : 여러명의 이름과 나이를 입력 받아서 csv 형식으로 파일에 저장 # csv란? 데이터(속성)를 ,(쉼표) 구분 하고 행을 \n (줄바꿈) 으로 구분하는 형식

personlist = '' # 여러명의 사람들 정보를 가지는 문자열(csv 형식)
while True :
    name = input('name : ')
    if name == 'x' :
        break
    age = input('age : ')
    person = name + ',' + age
    personlist += person + '\n'

