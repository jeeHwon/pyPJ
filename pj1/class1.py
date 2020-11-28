# class 클래스명 :
#     메서드()
#     메서드()

# class Car:
#     def __init__(self, t, c):
#         print('생성자')
#         self.type = t
#         self.color = c

#     def __del__(self):
#         print('소멸자')

#     def showInfo(self):
#         print(self.type+', '+self.color)

#     def tuning(self, c):
#         self.color = c
#         self.showInfo()
        

# c1 = Car('coupe', 'red')
# c2 = Car('suv', 'yellow')
# c1.showInfo()
# c2.showInfo()
# print('c1 tuning -> black')
# c1.tuning('black')
# print('\n'*30)

# 다중상속
class X(object):
    pass
class Y:
    pass
class Z():
    pass

# 모두 object를 상속받음
print('상속관계:', X.mro())
print('상속관계:', Y.mro())
print('상속관계:', Z.mro())
print('='*60)

class A(X, Y):
    pass
class B(Y, Z):
    pass
class C(A, B): # 너무 복잡한 다중상속은 코드 해석이 어려움
    pass

print('상속관계:', A.mro())
print('상속관계:', B.mro())
print('상속관계:', C.mro())
print('='*60)

class Car:
    def __init__(self, type, color):
        self.type = type
        self.color = color
    
    def show(self):
        print('Car class show method', self.type, self.color)

class KiaCar(Car):
    def __init__(self, carname, type, color):
        super().__init__(type, color)   #부모 생성자 호출
        self.carname = carname
    
    def show(self):
        print('KiaCar class show method',self.type, self.color, self.carname)
    
    def tuning(self, color):
        self.color = color
        self.show()

class HyundaiCar(Car):
    def __init__(self, carname, type, color):
        super().__init__(type, color)   #부모 생성자 호출
        self.carname = carname
    
    def show(self):
        print('HyundaiCar class show method',self.type, self.color, self.carname)
    
    def tuning(self, color):
        self.color = color
        self.show()

k1 = KiaCar('k9', 'sedan', 'black')
print(k1.carname)
k1.show()
k1.tuning('gray')

h1 = HyundaiCar('gv80', 'suv', 'red')
h1.show()
print('='*60)

import cx_Oracle
class DBManeger:
    def __init__(self):
        self.con = cx_Oracle.connect('happy/day@localhost:1521/xe')
        self.cur = self.con.cursor()
        print('연결성공')
    def __del__(self):
        print('연결해제')
        self.con.close()

    def makeDict(self):
        # cur.description 커서 속성 [(컬럼명1, 데이터타입, 속성1...),(컬럼명2..)]
        # print('self.cur.description',self.cur.description)
        # for colinfo in self.cur.description:
        #     print(colinfo[0])
        # 위를 한줄요약 하면 아래 : comprehension
        colnames = [colinfo[0] for colinfo in self.cur.description]    
        # print(colnames) # ['NO', 'TITLE', 'RATING', 'REGDATE']
        # print(cur.fetchall())
        templist =[]
        for datas in self.cur.fetchall():
            # print(datas)
            # print(colnames)
            temp={}
            for k, v in zip(colnames, datas):
                temp[k] = v
            templist.append(temp)
        # print(templist)
        return templist

                
        # def createRow(*arg):
        #     print('createRow() 함수')
        # return createRow()

        
    def selectAll(self):
        sql = "select * from webtoon order by no"
        self.cur.execute(sql)
        result = self.makeDict()
        for row in result:
            # print(row)
            print(row['NO'],row['TITLE'],row['RATING'],row['REGDATE'])

        # rows = self.cur.fetchall()
        # for row in rows:
        #     print(row[0],row[1],row[2],row[3])


    def selectJob(self):
        pass


    def selectRating(self, rating):
        sql = "select * from webtoon where rating >={} order by no"
        self.cur.execute(sql.format(rating))
        result = self.makeDict()

        for row in result:
            # print(row)
            print(row['NO'],row['TITLE'],row['RATING'],row['REGDATE'])

        # rows = self.cur.fetchall()
        # for row in rows:
        #     row = list(row)
        #     print(row)

    def insert(self, title, rating, regdate):
        sql = "insert into webtoon values (webtoon_seq.nextval,'{}','{}','{}') "
        self.cur.execute(sql.format(title, rating, regdate))
        self.con.commit()


    def update(self, rating, regdate):
        sql = "update webtoon set regdate='{}' where rating >={}"
        self.cur.execute(sql.format(regdate, rating))
        self.con.commit()

        
    def delete(self, no):
        sql = "delete from webtoon where no={}"
        self.cur.execute(sql.format(no))
        self.con.commit()
        

o1 = DBManeger()
# o1.insert('test', '3', '2020-11-25')
# o1.delete('862')
# o1.selectAll()
o1.selectRating(9.99)
# o1.update('9.99', '2020.11.25')

# color = ['red', 'green', 'blue']
# fruit = ['apple', 'orange', 'grape']
# number = [1,2,3]
# for t in zip(color, fruit):
#     print(color, fruit)
# for t in zip(color, number):
#     print(color, number)
# for c, f, n in zip(color, fruit, number):
#     print(color, fruit, number)
