# [1] csv 파일 읽어 오기
file = open('인천광역시 부평구_인구 현황_20240214.csv','r')
    # csv 파일 경로 : 다운로드 받은 csv 파일명과 확장자를 넣는다
    # 'r' 읽기 모드
# print(file.read())
# .read() 읽어 온 파일의 모든 내용을 가져 오는 함수

# [2] csv 파일 내 모든 내용들을 가져온다
contents = file.read()

# [3] 줄 단위로 구분해서 리스트에 반환 한다
contentList = contents.split('\n')

# [4] 반복문을 이용한 리스트 내 요소들을 하나씩 호출 해보기
sum = 0 # 부평구 총 인구수를 저장 하는 변수
for row in contentList [1 : -2]:
    # print(row)
    cols = row.split(',')
    # print(cols)
    # print(cols[0])
    print(cols[1])
    sum += int(cols[1])
print(f'부평구의 총 인구수 : {sum}')