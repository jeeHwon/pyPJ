import pymysql as my
import os


conn = my.connect(host='localhost', port=3307, user='root', password='1234', db='pythondb', charset='utf8')
cur = conn.cursor()
sql = "insert into daydepdelay (dayOfWeek, cnt) values ('{}', {})"

with open(os.path.join('C:\\', 'study', 'mapreduce','day2007.csv')) as f:
	for line in f.readlines():
		data = line.split(',')
		print(data[0], data[1])

		cur.execute(sql.format(data[0], data[1]))
	conn.commit()
conn.close()
