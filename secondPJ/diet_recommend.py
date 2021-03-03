import pandas as pd
# db에서 nut와 food_list 가져오기

# DB 기본 연결 정보
import mysql.connector
config = {
    "user": "root",
    "password": "1234",
    "host": "sarte.kr", #local
    "database": "food", #Database name
    "port": "3306" #port는 최초 설치 시 입력한 값(기본값은 3306)
}

# id별 필요 영양소를 정보 받아와 리스트로 반환
def get_people_nut(nut_id):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        sql = f"SELECT * FROM nutrition where nut_id = {nut_id}"
        cursor.execute(sql)
        resultList = cursor.fetchall()  
        print(f"선택한 옵션: {resultList[0][2]}")
        return list(resultList[0])
    except mysql.connector.Error as err:
        print(err)
        return False

# cate3를 입력받아 100개 음식 정보 2차원 리스트로 반환
def get_100_foods(cate3):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        sql = f"SELECT * FROM food WHERE food_cate1 = '음식' and food_cate3 = '{cate3}' ORDER BY RAND() LIMIT 100"
        cursor.execute(sql)
        resultList = cursor.fetchall() 
        food_list = []
        print("="*30, f"선택된 {cate3} 음식 리스트", "="*30)
        for result in resultList:
            print(result[5], end=',')
            food_list.append(list(result))
        print("\n")
        return food_list
    except mysql.connector.Error as err:
        # print(err)
        return False

def get_food_list():
    global food_list
    food_cates = ['반찬1','주식','국물','반찬2','반찬3','부식']
    for food_cate in food_cates:
        food_list.append(get_100_foods(food_cate))


# id별 필요영양소를 lb, ia, ub로 나눠서 리턴
def get_nut_list(nut_id):
    array = get_people_nut(nut_id)
    nut_lb = [array[6]*0.9]
    nut_ia = [array[6]*1.0]
    nut_ub = [array[6]*1.1]
    print(array)
    # lb, ia, ub가 세개씩 반복되는 index 7번부터 나눠서 리스트에 담아 반환
    for i in range(7, len(array)-2, 3):
        nut_lb.append(array[i])
        nut_ia.append(array[i+1])
        nut_ub.append(array[i+2])
    return nut_lb, nut_ia, nut_ub


nut_lb, nut_ia, nut_ub = get_nut_list(4)


def get_food(nut_idx, cur_cate):
    global food_list
    temp = []
    cate_idx = -1
    for i in range(len(cur_cate)):
        if cur_cate[i] :
            continue
        else: 
            temp.extend(food_list[i])
            cate_idx = i
            break
    df = pd.DataFrame(temp)
    top_food = df.iloc[df[nut_idx+7].idxmax()].tolist()
    return top_food, cate_idx

def is_under_ub(food, cur_nut, nut_ub):
    for i in range(len(cur_nut)):
        if nut_ub[i] == 0:
            continue
        if cur_nut[i] + food[i+7] > nut_ub[i]:
            return False
    return True

def add_food(food, cate_idx):
    global cur_nut, meals, cur_cate, food_list
    for i in range(len(cur_nut)):
        cur_nut[i] += food[i+7]
    meals.append(food)
    cur_cate[cate_idx] = True
    food_list[cate_idx].remove(food)

def add_rejection(nut_idx):
    global cnt_rejection, meals, cur_cate
    cnt_rejection[nut_idx] += 1
    if cnt_rejection[nut_idx] == 4:
        if len(meals) == 0:
            cnt_rejection = [0 for _ in range(27)]
            return
        df = pd.DataFrame(meals)
        top_food = df.iloc[df[nut_idx+7].idxmax()].tolist()
        meals.remove(top_food)
        for i in range(len(cur_nut)):
            cur_nut[i] -= top_food[i+7]
        food_cates = ['반찬1','주식','국물','반찬2','반찬3','부식']
        cate_idx = food_cates.index(top_food[4])
        cur_cate[cate_idx] = False
        cnt_rejection[nut_idx] = 0
        print(nut_list[nut_idx],f'4회 초과 ====> {top_food[5]}삭제')

def del_from_foodlist(food, cate_idx):
    global food_list
    food_list[cate_idx].remove(food)
    print("$"*30)

def check_nut(nut_lb, cur_nut, cur_cate, nut_ub):
    global nut_list, cnt_rejection, food_list
    for i in range(len(nut_lb)):
        if cur_nut[i] >= nut_lb[i]:
            continue       
        food, cate_idx = get_food(i, cur_cate)
        print('후보음식',food[5])
        if is_under_ub(food, cur_nut, nut_ub):
            print(f'영양성분 만족 ====> [{food[4]}]',food[5])
            add_food(food, cate_idx)
            return True
        elif len(meals) == 0:
            del_from_foodlist(food, cate_idx)
            continue
        else:
            del_from_foodlist(food, cate_idx)
            print(nut_list[i],f'초과 ====> {cnt_rejection[i]+1}회 거절')
            add_rejection(i)
            continue
    return False

def is_finish():
    global cur_cate, cur_nut
    for cate in cur_cate:
        if cate == False:
            return False
    return True
def out_meal():
    global meals
    print("=================오늘의 식단=================")
    for meal in meals:
        print(meal[4],meal[5])
    # print('필요영양소',nut_lb)
    # print('식단영양소',cur_nut)

food_list = []
get_food_list()
meals = []
cur_nut = [0 for _ in range(27)]
cnt_rejection = [0 for _ in range(27)]
cur_cate = [False for _ in range(6)]
# cur_cate = [True, True, True, True, False, False]
nut_list = ['칼로리','탄수화물','식이섬유','지방','리놀레산','a-리놀레산','단백질',
            '비타민A','비타민D','비타민E','비타민K','비타민C','티아민',
            '리보플라빈','비타민B6','엽산','비타민B12','판토텐산','비오틴',
            '칼슘','인','나트륨','칼륨','마그네슘','철','아연','구리'
]

i = 0
while True:
    if i == 500:
        break
    if i % 10 == 0:
        get_food_list()
        meals = []
        cur_nut = [0 for _ in range(27)]
        cnt_rejection = [0 for _ in range(27)]
        cur_cate = [False for _ in range(6)]
    if is_finish():
        out_meal()
        break
    check_nut(nut_lb, cur_nut, cur_cate, nut_ub)
    i += 1
# print(cur_nut)
# print(cur_cate)



