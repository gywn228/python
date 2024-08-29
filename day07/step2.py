# 딕셔너리
# - 사전 이라는 뜻
# - key 와 value 값 으로 하는 한쌍을 여러개 저장 하는 자료 구조
'''
    리스트의 부족 한 점
        - 저장된 순서 번호 (인덱스) 와 요소(값) 저장 되는 구조
        - 인덱스는 숫자로 구성된 순서 번호 이므로 대량의 인덱스는 사람이 식별이 어렵다.

'''
# - 딕셔너리의 형태
# - { key : value , key : value , key : value }
# key와 value 를 :(콜론) 으로 구분 하여 한쌍을 이루는 여러 쌍 들을 중괄호 감싼 형식

# [1] 딕셔너리 선언
dic = {'name' : '김효주', 'phone' : '010-1234-5678', 'birth' : 1999}
dic2 = {1 : 'h1'} # key는 문자와 숫자도 가능 하다
dic3 = {'a' : {'b' : 'h2'}} # 딕셔너리 안에 딕셔너리가 중첩이 가능 하다
dic4 = {'a' : [1,2,3]} # 'a' 라는 key에 리스트 자료가 1개(value) 존재 한다

# [2] 딕셔너리의 한 쌍 추가/수정 # 딕셔너리 타입 : 변수명['key'] = 값 # 만약에 key가 존재하면 수정, key가 존재하지 않으면 추가
dic['addr'] = '인천시' # dic(딕셔너리)에 'addr' 이라는 key와 '인천시' 갖는 value 를 한쌍 으로 해서 딕셔너리에 추가
print(dic)
    # value 수정      # 변수명['key'] = 새로운 값
dic['name'] = '효주'
print(dic)
    # 한쌍 삭제     # del 변수명['key'] # 지칭한 key의 쌍(key:value)을 제거한다
del dic['addr'] # del 키워드 [키워드란? 파이썬 에서 미리 만들어진 기능이 담긴 단어 들 = for , if , del 등등]

# [3] 딕셔너리 만들 때 주의 할 점
# a = {1 : 'a' , 1 : 'b'} # 1. 중복된 key의 이름을 가질 수 없다.
    # 왜? key는 여러 쌍 들 중에서 value의 구분(식별) 용도로 사용 하기 때문에
# a = {[1,2] : 'h1'}      # 2. 리스트(객체) 타입 으로는 key를 사용 할 수 없다

# [4] 딕셔너리 에서 key를 이용한 value 반환/추출 , # 변수명['key']
print(dic['name']) # 효주
# print(dic['age']) # 오류 발생 : KeyError: 'age' # 존재 하지 않는 key

# [5] 딕셔너리의 관련 함수들 # 함수/기능 란? 입력에 따른 기능 처리 후 결과를 반환 하는 구조
    # print('aa') # 'aa' 라는 print 함수 에게 입력(인자값) 전달 하여 console 출력 (기능 처리) 후 반환 하는 구조
    # int('3')    # '3' 라는 int 함수 에게 입력(인자값) 전달 하여 타입 변환(기능 처리) 후 반환 (변환 된 정수 값) 하는 구조

# 1. .keys() : 딕셔너리 내 모든 key 들을 모아서 객체로 반환 해주는 함수
print(dic.keys()) # dict_keys(['name' , 'phone' , 'birth'])
# 2. list(자료) : 지정한 자료의 타입을 리스트 타입 으로 변환 하는 함수
print(list(dic.keys())) # ['name', 'phone', 'birth']
# 3. .values() : 딕셔너리 내 모든 value 들을 모아서 객체 로 반환 해주는 함수
print(dic.values()) # dict_values(['효주', '010-1234-5678', 1999])
# 4.
print(list(dic.values())) # ['효주', '010-1234-5678', 1999]
# 5. .items() : 딕셔너리 내 모든 쌍(key:value)을 튜플로 묶은 객체로 변환 해주는 함수
print(dic.items()) # dict_items([('name', '효주'), ('phone', '010-1234-5678'), ('birth', 1999)])
# 6.
print(list(dic.items())) # [('name', '효주'), ('phone', '010-1234-5678'), ('birth', 1999)]
# 7. .get('key') : 딕셔너리 내 key에 해당 하는 value 값을 반환 함수
print(dic.get('name')) # == dic['name'] 동일 한 방법 # 차이점 이 있다
#print(dic['age'])  # 딕셔너리 내 존재 하지 않는 key 호출 하면 오류 발생
print(dic.get('age')) # 딕셔너리 내 존재 하지 않는 key 호출 하면 None ( 자료가 없다는 뜻 가진 키워드) 반환 한다 (*좀 더 안전한 프로그램 구현 가능)
# 8. key in 딕셔너리 : 딕셔너리 내 key가 존재 하면 True 존재 하지 않으면 False
print('name' in dic) # True # 딕셔너리 내 'age'라는 key가 존재 해서 True 변환 됨
print('age' in dic) # False # 딕셔너리 내 'age'라는 key가 없어서 False 변환 됨
# 9. len(딕셔너리) : 딕셔너리 내 쌍(key:value) 총 개수
print(len(dic))
