import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 그래프 한글처리(from matplotlib import font_manager, rc)
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

tips = sns.load_dataset('tips')
# print(tips)

# 불린 추출
# print(tips['sex']=='Female')
# print(tips[tips['sex']=='Female'])
# print(tips['total_bill'].mean())
# print(tips['total_bill']>tips['total_bill'].mean())
# print(tips[tips['total_bill']>tips['total_bill'].mean()])

# plt 기본
# plt.plot([1,2,3], [10,20,30])        # plt.plot(x좌표, y좌표) -> default 선그래프 형태
# plt.plot([1,2,3], [10,20,30], 'o')   # 'o' -> 점그래프 형태
# plt.plot([10,20,30,60], 'o')         # 1차원이면 x임의 값으로 설정하고 y값으로 인식함
# plt.plot([10,20,30,60], 'o--')       # 'o--'-> 점과 잇는 점선
# plt.show()                           # 그래프 출력

# plt naming
# plt.plot([1,2,3,4,5],[10,20,40,78,150])
# plt.title('선그래프')                  # 그래프 제목
# plt.xlabel('x값')                     # x축 제목
# plt.ylabel('y값')                     # y축 제목
# plt.xticks([1,3,5])                   # x축 값
# plt.yticks([10,20,30])                # y축 값
# plt.xlim(-5,5)                        # x축 값 범위(min, max)
# plt.show()

# # anscombe 데이터는 4개의 그룹이 평균, 분산, 상관관계, 회귀선이 동일
# ans = sns.load_dataset("anscombe")
# # print(ans)
# g1 = ans[ans['dataset']=='I']
# g2 = ans[ans['dataset']=='II']
# g3 = ans[ans['dataset']=='III']
# g4 = ans[ans['dataset']=='IV']

# # 1. 빈 플롯 생성
# fig = plt.figure()
# # 2. 그래프 영역 설정
# a1 = fig.add_subplot(2, 2, 1)   # 2행 2열 1번째 그래프
# a2 = fig.add_subplot(2, 2, 2)   # 2행 2열 2번째 그래프
# a3 = fig.add_subplot(2, 2, 3)   # 2행 2열 3번째 그래프
# a4 = fig.add_subplot(2, 2, 4)   # 2행 2열 4번째 그래프
# # 3. 그래프 추가
# a1.plot(g1['x'], g1['y'], 'ro') # 빨간점
# a2.plot(g2['x'], g2['y'], 'go') # 초록점
# a3.plot(g3['x'], g3['y'], 'bo') # 파란점
# a4.plot(g4['x'], g4['y'], 'yo') # 노란점
# # 4. 옵션
# a1.set_title('group1')  # subplot 타이틀 설정
# a2.set_title('group2')
# a3.set_title('group3')
# a4.set_title('group4')
# fig.tight_layout()      # 각 타이틀 안겹치게
# fig.suptitle('ANSCOMBE Test')
# plt.show()

# fig = plt.figure()
# a1 = fig.add_subplot(1,1,1)
# a1.plot([1,2,3],[10,20,30])
# a1.set_title('graph')
# a1.set_xlabel('x')
# a1.set_ylabel('y')
# plt.show()

# tips -> 그래프로
# print(tips)
# plt.plot(tips['total_bill'],'o')
# plt.ylabel('식대')
# plt.show()

# 히스토그램 : 변수 1개를 사용하여 구간별 분포 표시(일변량 그래프)
# print(tips['total_bill'].min()) # 식대 최소값 : 3.07
# print(tips['total_bill'].max()) # 식대 최대값 : 50.81
# plt.hist(tips['total_bill'], bins=30)   # x축의 간격(30구간으로 나누어 표시)
# plt.title('식대 히스토그램')
# plt.show()

# 산점도 : 변수 2개를 사용해서 분산 정도를 표시(이변량 그래프)
# plt.scatter(tips['total_bill'],tips['tip'])
# plt.title('식대-팁 산점도')
# plt.xlabel('식대')
# plt.ylabel('팁')
# plt.show()

# 사분위수 - Box-plot
# print("여성이 계산한 데이터\n", tips[tips['sex']=='Female'])
# print("여성이 지급한 팁\n", tips[tips['sex']=='Female']['tip'])
# plt.boxplot(tips[tips['sex']=='Female']['tip'])
# plt.title('여성이 지급한 팁')
# plt.show()
# plt.boxplot(tips[tips['sex']=='Male']['tip'])
# plt.title('남성이 지급한 팁')
# plt.show()
# plt.title('성별에 따라 지급한 팁')
# plt.xlabel('성별')
# plt.ylabel('금액')
# plt.boxplot([tips[tips['sex']=='Female']['tip'],tips[tips['sex']=='Male']['tip']], labels=['여자', '남자'])
# plt.show()

# 산점도 - 옵션추가
# def getSex(sex):
#     if sex=='Female':
#         return 0
#     else:
#         return 1
# tips['sexToNum'] = tips['sex'].apply(getSex)  
# print(tips)
# plt.scatter(tips['total_bill'],tips['tip'])  
# plt.scatter(tips['total_bill'],tips['tip'], s=tips['size']*15)   # s => 1개의 변수 추가하여 점 크기 다르게
# plt.scatter(tips['total_bill'],tips['tip'], alpha=0.5)           # alpha => 투명도
# plt.scatter(tips['total_bill'],tips['tip'], c=tips['sexToNum'])  # c => 1개의 변수 추가하여 색 다르게
# plt.title('식대-팁 산점도')
# plt.xlabel('식대')
# plt.ylabel('팁')
# plt.show()


data = pd.read_csv('data/accidentdata.csv')
d1 = data[data['사상자수']>=3]
# print(d1)
# 1) 일요일 사상자수의 최대값과 최소값 출력
print(d1[d1['요일']=='일']['사상자수'].min())
print(d1[d1['요일']=='일']['사상자수'].max())

# 2) 일요일 교통사고 사상자수 분포를 상자그림으로
plt.boxplot(d1[d1['요일']=='일']['사상자수'])
plt.title('일요일 교통사고 사상자수')
plt.xlabel('요일')
plt.ylabel('사상자수')
plt.ylim(0, 20)
plt.show()

# 3) 요일별 교통사고 사상자수를 상자그림으로
list = ['일','월','화','수','목','금','토']
arr = []
for i in range(len(list)):
    arr.append(d1[d1['요일']=='{}'.format(list[i])]['사상자수'])
plt.boxplot(arr, labels=list)
plt.title('요일별 교통사고 사상자수')
plt.xlabel('요일')
plt.ylabel('사상자수')
plt.ylim(0, 20)
plt.show()
