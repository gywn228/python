# 주제 : 전화번호부 구현하기 * csv 파일로 영구 저장
    # 조건1 : 등록시 이름과 전화번호를 입력받아 csv 파일에 저장하기
    # 조건2 : 목록시 모든 csv 파일 내 이름과 전화번호를 출력하기
import csv
# 전화번호 목록 리스트
phoneBooks = []

# [1] 무한 루프/반복
while True :
    ## -----------------csv 파일 읽어 오기----------------------##
    file = open('phoneBooks.csv', 'r')  # 1. 파일 읽기 모드로 파일 객체 반환
    contents = csv.reader(file)  # 2. 파일 객체를 csv 객체로 읽어 오기
    phoneBooks = list(contents)  # 3. 읽어온 객체를 list 타입 으로 반환 # list(): list 타입 으로 변환 해주는 함수
    file.close()
    ## -------------------------------------------------------##
    # 들여 쓰기 주의
    # [2] 기능 입력 받기
    choose = input('1.등록 2.목록 3.종료 : ')
    # [3] 입력 조건문
    if choose == '1' :
        print('>>> 전화번호 등록 >>>')
        # [4] 입력 받기
        name = input('> name : ')
        phone = input('> phone : ')
        phoneBooks.append([name , phone])
    # [5] 파일 쓰기 모드

    if choose == '2' :
        print('>>>전화번호 목록 >>>')

        # 2차원 리스트 출력 하기
        for row in phoneBooks :     # 2차원 리스트 출력 하기 # 2차원 리스트를 반복문 이용한 자료 반환 하기
            print(row)
    if choose == '3' :
        break # 가장 가까운 반복문을 종료/탈출 한다 # 즉 무한루프 종료
 ## --------------------csv 파일 쓰기-----------------------
    file = open('phoneBooks.csv', 'w', newline="")
    csvFile = csv.writer(file, delimiter=',')
    # csvFile.writerow([name, phone])
    csvFile.writerows(phoneBooks)       # csv 내용 쓰기
    file.close()
 ## -------------------------------------------------------
