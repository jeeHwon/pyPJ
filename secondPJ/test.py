import pandas as pd
import sqlite3
import pymysql
pymysql.install_as_MySQLdb()
import sqlalchemy

from sqlalchemy import create_engine
engine = create_engine("mysql+mysqldb://root:"+"1234"+"@sarte.kr/food", encoding='utf-8')
conn = engine.connect()


nu=pd.read_csv('data\\nu3.csv',delimiter=',',encoding='cp949')

print(nu)
nu.to_sql(name='food_all',
          con=engine,
          if_exists='append',
          dtype = {
                    'food_no': sqlalchemy.types.INTEGER(),
                    'food_code': sqlalchemy.types.VARCHAR(100),
                    'food_dae': sqlalchemy.types.VARCHAR(100),
                    'food_name': sqlalchemy.types.VARCHAR(100),
                    'food_jung': sqlalchemy.types.VARCHAR(100),
                    'food_so': sqlalchemy.types.VARCHAR(100),
                    'food_il': sqlalchemy.types.VARCHAR(100),
                    'food_dan': sqlalchemy.types.VARCHAR(100),
                    'food_kcal': sqlalchemy.types.NUMERIC(),
                    'food_pro': sqlalchemy.types.NUMERIC(),
                    'food_fat': sqlalchemy.types.NUMERIC(),
                    'food_carbo': sqlalchemy.types.NUMERIC()
                     })