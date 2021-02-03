# 데이터 전처리
# 범주형데이터 : 정해진 값 만을 가질 수 있음 ex) 연령대(20,30대..), 성별, 지역(서울,제주..)
# 수치형데이터 : 다양한 숫자값을 가짐 ex) 나이, 키
city = c('서울','대전','서울','제주','대전')
city = factor(city)
levels(city)

# 변수의 요약
g = c('남','여','여','남','여','여','남','여')
g = factor(g)
levels(g)
length(g)
t1 = table(g)    # 절대빈도표
t1
t1/length(g)     # 상대빈도

prop.table(t1)
barplot(t1)     # 막대그래프
pie(t1)         # 원그래프

# 수치형 변수의 요약
kor = c(60,78,83,74,100,85,95,80,70)
sort(kor)
sort(kor,decreasing = T)
min(kor)
max(kor)
median(kor)
mean(kor)
quantile(kor)
var(kor)  # 분산
sd(kor)   # 표준편차
boxplot(kor)
hist(kor)

# 구로구와 도봉구의 미세먼지 비교
library(readxl)
data <- read_excel("data/period.xlsx")
d1 = data %>% filter(측정소명 %in% c('구로구','도봉구'))
guro = subset(d1, 측정소명 =='구로구')
dobong = subset(d1, 측정소명 =='도봉구')
summary(guro)
boxplot(guro$미세먼지, dobong$미세먼지, main='미세먼지 비교', names=c('구로구','도봉구'))

# 구로구에서 치킨집이 많은 동네
data <- read_excel("data/chicken.xlsx")
head(data$소재지전체주소)
juso = substr(data$소재지전체주소,11,14)
juso = gsub("[0-9]","",juso)
juso = gsub(" ","",juso)
t = table(juso)
pie(t)
barplot(t)
head(data)

# 트리맵
install.packages("treemap")
library(treemap)
t
df <- as.data.frame(t)   # 데이터타입변환 as.xxxx
str(df)
treemap(df, index='juso', vSize='Freq', title='구로동 치킨집')


# 데이터 따로 저장
install.packages("xlsx")
library(xlsx)
data2 <- data
data2$동주소 = juso
head(data2$동주소)
write.xlsx(data2, 'data/chicken3.xlsx')


# 데이터 합치기
g1 = data.frame(no=c(1,2,3), kor=c(100,80,90))
g1
g2 <- data.frame(no=c(1,2,3), eng=c(80,70,60), mat=c(70,80,100))
g2
# 가로로 합치기
grade <- left_join(g1,g2,by='no')
grade
# 세로로 합치기
df1 <- data.frame(no=c(10,20), kor=c(88,77), eng=c(66,55), mat=c(70,80))
df1
student <- bind_rows(grade, df1)
student

# ---------
data <- mpg
data
fuel <- data.frame(fl=c('c','d','e','p','r'), price=c(100,200,150,300,250))
data <- left_join(data, fuel, by='fl')
data

# 두 수치형 변수
data <- read.csv('data/TWO_CONT.csv')
data
plot(data$HOUR, data$SCORE)
# 보조선
mean(data$HOUR)
abline(v=mean(data$HOUR), lty=1) # 가로 보조선 추가, linetype:실선
abline(h=mean(data$SCORE), lty=2)# 세로 보조선 추가, linetype:점선
cor(data$HOUR, data$SCORE)    # 상관계수

# 과제
library(ggplot2)
midwest # 미국 지역의 인구통계
data <- midwest
# 1) 전체인구대비 미성년인구백분율 변수 추가
data$perNotAdult <- (data$poptotal - data$popadults) / data$poptotal * 100
data[c('state','poptotal','popadults','perNotAdult')]

# 2) 미성년 인구 백분율이 가장 높은 지역 5개 출력
data[c('state','poptotal','popadults','perNotAdult')] %>% 
  arrange(desc(perNotAdult)) %>% head(5)

# 3) 미성년 비율 등급 변수를 추가
data$perNotAdultGrade <- ifelse(data$perNotAdult>=40, 'large',
                                ifelse(data$perNotAdult>=30, 'middle','small'))
data[c('state','poptotal','popadults','perNotAdult','perNotAdultGrade')]





