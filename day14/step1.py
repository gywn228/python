# [1] 파이썬에서 시각화 할수 있는 객체 모듈 가져오기
    # import : 현재 파일 외부에 있는 함수 또는 객체 가져오기 위한 키워드
    # as : 객체 또는 함수의 별칭 * 함수 또는 객체 이름이 길거나 복잡할때
import matplotlib.pyplot as plt

# - 다양한 시각화(차트) 옵션을 추가
plt.title('chart1') # [3] 차트 제목

YData = [5,2,7,1] # [4] y축 데이터
plt.plot(YData) # [5] 선차트에 y축 데이터를 대입

# [2] 시각화(차트) 실행
plt.show()


plt.title('chart2')
XData = [10, 20, 30, 40] # x축 데이터
YData = [50, 2, 9, 16] # y축 데이터
plt.plot(XData,YData) # x축과 y축 데이터를 선차트에 대입
plt.show()

# [3]
plt.title('chart3')
XData = ['cola' , 'cider' , 'fanta']
YData = [102 , 150 , 96]
plt.plot(XData,YData , label = 'sales')
plt.xlabel('product')
plt.ylabel('sales')
plt.grid()
plt.legend()
plt.show()