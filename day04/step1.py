'''
    입력함수 : input("프롬프트 문자")
    연산자 :
        1. 연결 연산자
        2. 비교 연산자
        3. 논리 연산자 : and,or,not
        4. 복합 대입 연산자 : = 대입, (산술 연산자)=연산후에 대입
'''
x = 10
y = 3
z = 1
# print(f'1.산술연산자 : {x+y},{x-y},{x*y},{x/y},{x//y},{x%y},{x**y}')
# print(f'2.비교연산자 : {x>y},{x<y},{x>=y},{x<=y},{x==y},{x!=y}')
# print(f'3.논리연산자 : {x>=y and y <= z},{x>=y or y<=z},{not(x>=y)}')
# x+=2
# print(x)#12
# x %= 7
# print(x)#5

#[1]
money = int(input("금액입력 : "))
sipman = money // 100000
man = (money - sipman * 100000) // 10000
chun = (money - (sipman * 100000 + man * 10000 )) // 1000
print(f'결과 : 십만원권:{sipman}개, 만원권:{man}개, 천원권:{chun}개')

#[2]
korean = int(input("국어 점수 입력 : "))
eng = int(input("영어 점수 입력 : "))
math = int(input("수학 점수 입력 : "))
point = '국어 우수' if (korean + eng + math) / 3 >= 90 and korean >= 95 else '장려'
print(point)
