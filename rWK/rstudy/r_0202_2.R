install.packages("rgdal")
install.packages("sp")

library(sp)
library(rgdal)
library(dplyr)
library(readxl)

# 데이터 읽어 최소한의 컬럼 추출
data <- read_excel("data/chicken.xlsx")
head(data$소재지전체주소)
juso = substr(data$소재지전체주소,11,14)
juso = gsub("[0-9]","",juso)
juso = gsub(" ","",juso)
data$동주소 = juso
data <- rename(data, 'X좌표'='좌표정보(X)')
data <- rename(data, 'Y좌표'='좌표정보(Y)')
data <- data[c('번호','동주소','사업장명','시설총규모','X좌표','Y좌표')]
data
dim(data)

# null 처리 후 자료형변환
data <- data %>% filter(is.na(X좌표)==FALSE, is.na(Y좌표)==FALSE)
data$X좌표 <- as.numeric(data$X좌표)
data$Y좌표 <- as.numeric(data$Y좌표)
str(data)
write.csv(data,file='data/chicken.csv')

# CRS Function(long:경도, lat:위도)
convertCRS <- function(long, lat, from.crs, to.crs){
  xy <- data.frame(long=long, lat=lat)
  coordinates(xy) <- ~long+lat
  
  from.crs <- CRS(from.crs)
  from.coordinates <- SpatialPoints(xy, proj4string=from.crs)
  
  to.crs <- CRS(to.crs)  
  changed <- as.data.frame(SpatialPoints(spTransform(from.coordinates, to.crs)))
  names(changed) <- c("long","lat")
  
  return(changed)
}

from.crs <- "+proj=tmerc +lat_0=38 +lon_0=127 +k=1 +x_0=200000 +y_0=500000 +ellps=bessel +units=m"
to.crs <- "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs"

# 위도 경도를 convert해 데이터프레임에 추가
coord <- data.frame(grs.long=data[,4], grs.lat=data[,5])
temp <- convertCRS(coord$X좌표, coord$Y좌표, from.crs, to.crs) # error 발생!
data$long = temp$long
data$lat = temp$lat

# 파일 저장
library(xlsx)
write.xlsx(data, 'data/chicken_re2.xlsx')
summary(data)
