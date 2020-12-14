import pymysql as my
import os


conn = my.connect(host='localhost', port=3307, user='root', password='1234', db='pythondb', charset='utf8')
cur = conn.cursor()
sql = 'insert into depdelay (yy, mm, cnt) values ({}, {}, {})'

with open(os.path.join('C:\\', 'study', 'mapreduce','result2007.csv')) as f:
	for line in f.readlines():
		data = line.split(',')
		print(data[0], data[1], data[2].strip())
		cur.execute(sql.format(data[0], data[1], data[2].strip()))
	conn.commit()
conn.close()
