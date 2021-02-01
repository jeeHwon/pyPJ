# 벡터의 연산
a<-c(1,2,3,4)
b<-c(5,6,7,8)
c<-a+b
c
c<-a*b

# 길이가 다른 벡터연산(벡터길이 서로배수) => 짧은 벡터가 반복되어 계산
b<-c(5,6)
c<-a+b
c<-a*b

# 길이가 다른 벡터연산(벡터길이 서로배수X) => 경고 메시지 + 계산
a<-c(1,2,3,4)
b<-c(5,6,7)
c<-a+b
c<-a*b

# 데이터프레임 : 벡터들을 조합한 형태
id<-c('f1','f2','f3','f4')
name<-c('보라돌이','뚜비','나나','뽀')
age<-c(10,20,30,40)
isBoy<-c(T,T,F,F)


# 데이터프레임 생성함수
df<-data.frame(id,name,age,isBoy,stringsAsFactors = T)
df
str(df)

# 데이터접근
df[2,3]           # 2행 3열
df[c(2,3),]       # 2행,3행 모든열
df[c(2,3),c(2,4)] # 2행,3행, 2열,4열
df[,c(2,4)]       # 모든행, 2열,4열
df[c('name','age')]

# 열에 접근
df$age
df$name
df$name[3:4]

# 예제데이터
data()
iris

# 데이터저장
write.csv(iris,file='iris.csv')
write.csv(iris,file='iris.csv',row.names=F)
write.csv(df,file='df.csv')

# 데이터 읽기
data<-read.csv('df.csv')
data

# 엑셀 데이터 읽기
install.packages("readxl")
library(readxl)
a<-read_excel('test.xlsx')
a
a1<-read_excel('test.xlsx', sheet=2)
a1
a2<-read_excel('test.xlsx', sheet="Sheet2")
a2

# 클립보드에 있는 내용 가져오기
a3<-read.table("clipboard")
a3
a3<-read.table("clipboard", header = T)
a3
iris
str(iris)
nrow(iris)  # 행 수
ncol(iris)  # 열 수
head(iris,3)
tail(iris)
min(iris$Sepal.Length)        # 최소값
quantile(iris$Sepal.Length)   # 사분위수수
max(iris$Sepal.Length)        # 최대값
summary(iris)
View(iris)

# subset(데이터프레임, 조건, [조회하고 싶은열])
subset(iris,Sepal.Length>6)
subset(iris,Sepal.Length>6, c(1,5))
subset(iris,Sepal.Length>6, c('Sepal.Length','Species'))
subset(iris,Sepal.Length>6 | Sepal.Width>=3.5, c('Sepal.Length','Sepal.Width','Species'))
subset(iris,Sepal.Length>6 & Sepal.Width>=3.5, c('Sepal.Length','Sepal.Width','Species'))

# 꽃의 종류가 setosa 인 것의 정보를 요약
summary(subset(iris, Species=='setosa'))
summary(iris[iris$Species=='setosa',])
str(iris[iris$Species=='setosa',c('Sepal.Length')])            # 벡터
str(iris[iris$Species=='setosa',c('Sepal.Length','Species')])  # 데이터프레임

# dplyr 패지키
install.packages('dplyr')
library(dplyr)
data<-iris
data

# 컬럼명 변경
# rename(데이터프레임, 새변수명1=변수명1...)
data <- rename(data, len1=Sepal.Length, wid1=Sepal.Width)
head(data)

# 새 컬럼 생성
data$length <- data$len1 + data$Petal.Length
head(data)

# ifelse(조건,참인경우, 거짓인경우)
data$new <- ifelse(data$len1>5, 'good','low')
head(data)
data$new2 <- ifelse(data$len1>5, 'good', ifelse(data$len1>4.5, 'low', 'fail'))
head(data)
View(data)

# dplyr 패키지의 함수들
# %>% 파이프라인 앞명령어의 출력이 뒷명령어의 입력으로 처리
# rename : 컬럼명 변경
# filter(조건) : 조건에 맞는 데이터 추출
# select(열이름1,열이름2...) : 보고싶은 열 선택
# arrange(컬럼명) : 정렬
data8 <- head(data,10) %>% filter(new=='good')
data8 %>% select(Petal.Length, Petal.Width)
data8
head(iris,10) %>% filter(Sepal.Length>=5) %>% 
  select(Sepal.Length, Species) %>% arrange(desc(Sepal.Length))

# mutate(변수1=수식1, 변수2=수식2, ...) : 변수추가
head(iris) %>% mutate(hap=Sepal.Length+Petal.Length, 
                      avg=(Sepal.Width+Petal.Width)/2,
                      grade=ifelse(Sepal.Width>=3.5, 'good','poor')
                      )
# summarise() : 요약
# group_by(컬럼명) 
head(iris) %>% summarise(avg=mean(Sepal.Length))
iris %>% group_by(Species) %>% summarise(avg=mean(Sepal.Length))


# 과제
install.packages("ggplot2")
library(ggplot2)
View(mpg)

data <- mpg
head(data)
# 1) 자동차제조회사에 따라 도시연비의 평균출력
data %>% group_by(manufacturer) %>% summarise(avg=mean(cty))
# 2) cty, hwy의 평균연비변수를 추가
data$avg <- (data$cty+data$hwy)/2
# 3) 평균연비가 높은 데이터 3개 출력
head(data %>% arrange(desc(avg)), 3)  




