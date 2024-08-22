# 조건문 실습1 : 하나의 점수를 입력 받아서 점수가 80점 이상 이면 '합격' 아니면 '불합격' 출력
point = int(input("점수 입력 : "))
if point >= 80 :
    print('합격')
else:
    print('불합격')

# 조건문 실습2 :
    # 하나의 점수를 입력 받아 점수 변수에 지참 하기
    # 점수 변수가 90점 이상 이면 'A등급', 80점 이상 이면 'B등급' ,70점 이상 이면 'C등급' 그 외 '재시험 출력'

if point >= 90 :
    print('A등급')
elif point >= 80 :
    print('B등급')
elif point >= 70 :
    print('C등급')
else :
    print('재시험')

# 조건문 실습3 :
    # 3개의 점수를 입력 받아서 오름차순 으로 출력 하시오
point2 = int(input('첫번째 점수 입력 : '))
point3 = int(input('두번째 점수 입력 : '))
point4 = int(input('세번째 점수 입력 : '))
if point2 > point3 and point2 > point4 and point3 > point4 :
    print(f'{point2},{point3},{point4}')
elif point3 > point4 and point3 > point2 and point2 > point4 :
    print(f'{point3},{point2},{point4}')
elif point4 > point2 and point4 > point3 and point3 > point2 :
    print(f'{point4},{point3},{point2}')
elif point2 > point4 and point4 > point3 and point2 > point3 :
    print(f'{point2},{point4},{point3}')
elif point3 > point2 and point3 > point4 and point4 > point2:
    print(f'{point3},{point4},{point2}')
elif point4 > point2 and point4 > point3 and point2 > point3 :
    print(f'{point4},{point2},{point3}')
else:
    print('각기 다른 숫자를 입력해 주세요')
