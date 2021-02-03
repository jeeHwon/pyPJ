import numpy
import pandas as pd 
from pyproj import Proj, transform

df = pd.read_csv('../rWK/rstudy/data/chicken.csv', encoding='euc-kr')

# epsg:2097 -> epsg:4326 좌표 위경도 변환 코드
proj_UTMK = Proj('+proj=tmerc +lat_0=38 +lon_0=127 +k=1 +x_0=200000 +y_0=500000 +ellps=bessel +units=m +no_defs +towgs84=-115.80,474.99,674.11,1.16,-2.31,-1.63,6.43')
proj_WGS84 = Proj('epsg:4326')

df['lat'], df['long'] = transform(proj_UTMK, proj_WGS84, df['X좌표'], df['Y좌표'])
df.to_csv('data\\chicken_fin.csv')
print(df.head(10))
df.info()