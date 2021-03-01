
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
        sql = f"SELECT * FROM food WHERE food_cate3 = '{cate3}' ORDER BY RAND() LIMIT 20"
        cursor.execute(sql)
        resultList = cursor.fetchall() 
        food_list = []
        # print("="*30, f"선택된 {cate3} 음식 리스트", "="*30)
        for result in resultList:
            # print(result[5], end=',')
            food_list.append(list(result))
        # print("\n")
        return food_list
    except mysql.connector.Error as err:
        # print(err)
        return False

food_cates = ['반찬1','주식','국물','반찬2','반찬3','부식']
food_list = [] # [[반찬1리스트],[주식리스트]..] # 3차원 리스트
for food_cate in food_cates:
    food_list.append(get_100_foods(food_cate))

# id별 필요영양소를 lb, ia, hb로 나눠서 리턴
def get_nut_list(nut_id):
    array = get_people_nut(nut_id)
    nut_lb = [array[6]*0.9]
    nut_ia = [array[6]*1.0]
    nut_hb = [array[6]*1.1]
    print(array)
    # lb, ia, hb가 세개씩 반복되는 index 7번부터 나눠서 리스트에 담아 반환
    for i in range(7, len(array)-2, 3):
        nut_lb.append(array[i])
        nut_ia.append(array[i+1])
        nut_hb.append(array[i+2])
    return nut_lb, nut_ia, nut_hb

def clear_cate(cur_cate):
    for cate in cur_cate:
        if cate == 0:
            return False
    return True

def fit_food(cur_nut, cur_cate, food_list):
    cate_idx = -1
    for i in range(len(cur_cate)):
        if cur_cate[i] == 0:
            cate_idx = i
            break
    for food in food_list[cate_idx]:
        for i in range(len(cur_nut)):
            if cur_nut[i]+food[i+7] < nut_hb[i]:
                continue

nut_lb, nut_ia, nut_hb = get_nut_list(4)

POWER = True
cur_nut = [0 for _ in range(27)]
# cur_cate = [0 for _ in range(6)]
cur_cate = [1,1,0,0,0,0]
while True:
    if clear_cate(cur_cate):
        break
    if fit_food(cur_nut, cur_cate, food_list, nut_hb):
        pass
    break






