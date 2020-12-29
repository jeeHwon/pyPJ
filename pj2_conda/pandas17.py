from numpy.lib.shape_base import apply_along_axis
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from matplotlib import font_manager, rc

# 그래프 한글처리(from matplotlib import font_manager, rc)
fontname = font_manager.FontProperties(fname='C://myData//Fonts///malgun.ttf').get_name()
rc('font',family=fontname)

tips = sns.load_dataset('tips')
# print(tips.dtypes)

# ==자료형 반환(astype(), to_numeric())
# tips['newsex'] = tips['sex'].astype(str)
# tips['total_bill'] = tips['total_bill'].astype(str)
# print(tips)
# print(tips.dtypes)
tips10 = tips.head(10)
# print(tips10)
# print(tips10.dtypes)
# tips10.loc[[3,6,9],'total_bill']='not float'
# print(tips10)
# print(tips10.dtypes)

# tips10['total_bill'] = tips10['total_bill'].astype(float)                     # err(astype() -> not float 때문에 변환에러)
# tips10['total_bill'] = pd.to_numeric(tips10['total_bill'])                    # err(to_numeric() -> not float 때문에 변환에러)
# tips10['total_bill'] = pd.to_numeric(tips10['total_bill'], errors='corece')   # err 무시 NaN으로 바꿔
# tips10['total_bill'] = pd.to_numeric(tips10['total_bill'], errors='ignore')   # 데이터형 변환 X 
# tips10['total_bill'] = pd.to_numeric(tips10['total_bill'], errors='corece', downcast='float') 
# print(tips10)
# print(tips10.dtypes)
# tips.info()
# tips['sex'] = tips['sex'].astype(str)
# tips.info()
# tips['sex'] = tips['sex'].astype('category')     # str 타입보다 category는 메모리를 덜 사용
# tips.info()



# ==함수
def double(x):
    # print(x, '**')    # x에 시리즈 전달시 데이터 하나씩 받아와 함수적용
    return x*2
# print(double(7))    # 14

# == 시리즈. 데이터프레임에 함수 적용시 .apply(함수명)
# data = pd.DataFrame({'a':[1,2,3,4], 'b':[10,20,30,40]})
# # print(data)
# # s1 = data['a'].apply(double)
# # print(s1)
# # print(type(s1))
# # s2 = data['b'].apply(double)
# # print(s2)
# # print(type(s2))
# d1 = data.apply(double)     # 열 우선 실행
# print(d1)
# print("="*30)
# d2 = data.apply(double, axis=1) # 행 우선 실행
# print(d2)

# == tips에 함수적용
# def sexToNum(x):
#     if x =='Female':
#         return 1
#     else:
#         return 0

# tips['newsex'] =tips['sex'].apply(sexToNum)
# print(tips)

# 그룹에 함수적용
# def test1(x):
#     print(x)
#     print('***')
# tips10 = tips.sample(10, random_state=42)
# # print(tips10)
# # tips10['total_bill'].apply(test1)
# # g1 = tips10.groupby('sex')
# # g1.apply(test1)     # 그룹 객체에 함수 적용시 그룹 단위로 적용
# g2 = tips10.groupby(['sex', 'smoker'])
# g2.apply(test1)

# 성별별 식대의 큰금액 2개 추출
def getbill2(x):
    print(x)
    print(x.sort_values(by='total_bill',ascending=False)[:2])
g3=tips10.groupby('sex')
g3.apply(getbill2)
