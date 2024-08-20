''' 1. 연산자
 2. 연산자 종류
     연산자 1개당 연산 결과의 자료값 은 1개
     1. 산술 연산자 : +더하기, -뺴기, *곱하기, **제곱, /나누기, //몫, %나머지
     2. 연결 연산자 : +문자열 연결, ,(쉼표)문자열 연결
     3. 비교 연산자 : >초과, <미만, >=이상, <=이하, ==같다, !=같지 않다
     4. 논리 연산자 :
       and 이면서 면서 이고 그리고, 모두 True 이면 결과도 True 하나 라도 False 이면 결과도 False
       or 이거나 거나 또는 하나 라도, 하나 라도 True 이면 결과도 True
       not 부정 반대 , True -> False , False -> True
     5. 대입 연산자 : 
       1. = 오른쪽 값을 왼쪽에 대입
       2. +=, -=, ++=, /=, //=, %=
        -복합 대입 연산자
    
    
'''
# [1] 산술 연산자 , 반환 리터럴: 정수,실수 : 문자열 자료 1개
print( 10 + 3 ) #13
print( 10 - 3 ) #7
print( 10 * 3 ) #30
print( 10 ** 3) #제곱 1000
print( 10 / 3 ) #3.33333
print( 10 // 3 ) #3
print( 10 % 3 ) #1

# [2] 연결 연산자 , 반환 리터럴 : 문자열 자료 1개
print( "hello" + " python") #hello python
print( "hello" , "python") #hello python
#print( "hello" + " python"+3) #오류 발생

# [3] 비교 연산자 , 반환 리터럴 : 불리언 자료 1개
print( 10 > 3 ) # True
print( 10 < 3 ) # False
print( 10 >= 3 ) # True
print( 10 <= 3 ) # False
print( 10 == 3 ) # False
print( 10 != 3 ) # True

# [4] 논리 연산자
print( 10 > 3 and 20 > 15 ) #True
    # True and True => True
print( 10 > 3 and 20 > 30 ) #False
    # True and False => False
print( 10 > 3 or 20 > 15 ) #True
    # True or True => True
print( 10 > 3 or 20 > 30 ) #True
    # True or False => True
print( not (10 > 3) ) # True => False

# [5] 대입 연산자
var1 = 10 # 10 리터럴 값을 var1 변수에 대입.
#(1) var1 변수의 자료 값에 10을 더해서 저장
var1 + 10  #10   #var1 변수 값이 수정X
var1 = var1 + 10 #20
    # 1. var1 변수의 값호출 , var1 = 10 + 10
    # 2. 연산 , var1 = 20
    # 3. 대입 , var1 (20)
    # 짧게 작성 하는 방법
var1 += 10 #30
# 좌항 += 우항 : 우항의 값을 좌항 값과 더한 후 좌항에 대입
print(var1)
var1 -= 10 #20
print(var1)
var1 *= 10 #200
print(var1)
var1 **= 2 #40000
print(var1)
var1 /= 2 #20000.0
print(var1)
var1 //= 2 #10000.0
print(var1) 
var1 %= 3 # 1.0
print(var1)

# [6] 삼항 연산자 , 1.조건 2.참 3.거짓
    # [True 실행문] if [조건문] else [False 실행문]
        # 만약에 조건이 True 이면 [True 실행문] 실행
        # 만약에 조건이 False 이면 [False 실행문] 실행
    # 삼항 연산자 중첩
        #[True 실행문] if [조건문1] else [True 실행문2] if [조건문2] else [False 실행문]
point = 70
# 만약에 포인트 가 90 이상 이면 합격 아니면 불합격 으로 츨력
print('합격' if point >= 90 else '불합격')
# 만약에 포인트 가 90점 이상 이면 '최우수' 80점 이상 이면 '우수' 그외 '장려' 출력
    # 조건문1 : 포인트 가 90점이상
    # 조건문2 : 포인트 가 80점 이상
print('최우수' if point >= 90 else '우수' if point >= 80 else '장려')

# 실습1 : 기본급 과 수당 금액을 각 점수로 입력 받아 실수령 액 계산
# 실수령 액 계산법 : 기본급 + 수당 - 세금(기본급10%)
pay = int(input('기본급 : '))
pay2 = int(input('수당 : '))
pay3 = (pay + pay2) - pay * 0.1
print(f'실수령액 : {pay3}')