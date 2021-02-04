# tips 데이터의 요약 및 팁과 식대와의 관계
data <- read.csv("../../pj2_conda_wk/data/tips.csv")
data <- read.table('clipboard')
data <- read.csv("../../pj2_conda_wk/data/tips.csv", header=T)
data
summary(data)
plot(data$total_bill, data$tip)   # 산점도 그리기
cor(data$total_bill, data$tip)    # 양의 상관관계(0.6757)


# 시험점수
score=data.frame(kor=c(60,70,74,78,80,83,85,90,95,100),
                 mat=c(75,70,60,85,100,84,94,70,90,92))
summary(score)  
mean(score$kor)     # 국어 점수의 평균
mean(score$kor[score$kor >=90]) # 국어점수가 90점 이상인 것들의 평균
hist(score$kor) # 국어점수의 분포
boxplot(score$kor)
plot(score$kor, score$mat)  # 국어와 수학점수의 관계
cor(score$kor, score$mat)


# 선택하는 경우의수
choose(4,2)
choose(3,2)
choose(45,6)

# 치킨의 배달시간
bbq<-c(20,21,23,22,26,28,35,35,41,42,43,45,44,45,46,47,47,46,47,58,58,59,60,56,57,57,80)
bhc<-c(5,6,11,13,15,16,20,20,21,23,22,27,27,30,30,32,36,37,37,40,40,43,44,45,51,54,70,600)
mean(bbq)
mean(bhc)
summary(bbq)
summary(bhc)
boxplot(bbq,bhc)      # 이상치 발견
bhc <- bhc[bhc<600]   # 이상치 제거
summary(bhc)
boxplot(bbq,bhc)
hist(bbq)
hist(bhc)
var(bbq)  # 분산
var(bhc)
sd(bbq)   # 표준편차
sd(bhc)


# 과외 받기 전 후의 성적
bscore<-c(34,76,76,63,73,75,67,78,81,53,58,81,77,80,43,65,76,63,54,64,85,54,70,71,71,55,40,78,79,100,51,93,64,42,63,61,82,67,98,59,63,84,50,67,80,83,66,86,57,48)
ascore<-c(74,87,89,98,65,82,70,70,70,84,56,76,72,69,73,61,83,82,89,75,48,72,80,66,82,71,49,54,70,65,74,63,65,101,82,75,62,83,90,76,87,90,78,63,59,79,74,65,77,74)
length(bscore)
length(ascore)
boxplot(bscore, ascore)

# t검정 : 추출된 표본을 근거로 모집단을 추정해 모집단이 같은지 다른지 확인
t.test(bscore, ascore, var.equal=T)


# 통계검정
# 귀무가설 : 기존가설
# 대립가설 : 학자가 주장하는 바, 새로운 가설 
#   -> 귀무가설 잘못되었음을 증명하여 대립가설 채택 방식
# 유의확률(p-value) : 귀무가설이 참이라는 가정하에 얻은 통계랑, 귀무가설 지지 확률 
#   -> 유의확률이 작을수록 대립가설의 통계적 의미 증가. 0.05보다 작을 때 대립가설 채택


# 상관계수
# 두 수치형 변수의 관계
data <- read.csv('data/TWO_CONT.csv')
data
# 산점도
plot(data$HOUR, data$SCORE, col='blue')

# 보조선
mean(data$HOUR)
abline(v=mean(data$HOUR), lty=2)
abline(h=mean(data$SCORE), lty=2)
cor(data$HOUR, data$SCORE) # 상관계수, 양의 상관관계
cor.test(data$HOUR, data$SCORE)  # 상관계수를 검정해주는 함수 0.05보다 작으므로 상관계수 의미 있다


# 부자 관계 키의 상관관계
data = read.csv('data/heights.csv')
data
plot(data$father, data$son)
cor(data$father, data$son)
cor.test(data$father, data$son) # p-value 가 매우 작으므로 상관계수 의미있다

test <- c(1,2,3,4,5,6,7,8,9,10)
test2 <- c(1,2,3,4,5,6,7,8,9,9)
test2
plot(test, test2)
cor.test(test, test2)


# 도붕구, 구로구 공기의 질 
library(readxl)
library(dplyr)
data <- read_excel("data/period.xlsx")
d1 = data %>% filter(측정소명 %in% c('구로구','도봉구'))
guro = subset(d1, 측정소명 =='구로구')
dobong = subset(d1, 측정소명 =='도봉구')
summary(guro)
boxplot(guro$미세먼지, dobong$미세먼지, main='미세먼지 비교', names=c('구로구','도봉구'))
t.test(guro$미세먼지, dobong$미세먼지, var.equal=T)


# mpg 데이터 활용하여 경차와 suv 차량의 도시연비를 비교
# 경차와 suv 차량의 도시연비 차이가 유의미한지 판단
library(ggplot2)
library(dplyr)
data <- mpg
data <- data %>% filter(class=='suv' | class=='compact')
suv = subset(data, class =='suv')
compact = subset(data, class =='compact')
boxplot(suv$cty, compact$cty, main='도시연비 비교', names=c('suv','compact'))
t.test(suv$cty, compact$cty, var.equal=T)

# 이상치 처리
person = data.frame(name=c('jenny','seulgi','miyeon','sana'),
                   score=c(80,98,88,-94),
                   gender=c(1,1,4,1))
person
person['score'] >= 0 & person['score'] <=100
person <- person[person['score']>=0 & person['score']<=100,]
person$gender <- ifelse(person$gender==1 | person$gender ==2, person$gender, NA)
person

# 결측치 처리
is.na(person$gender) # 결측 유무 확인
!is.na(person$gender) # 결측 유무 확인
person <- person[!is.na(person$gender),]
person


# 이상치 처리
data <- iris
str(data)
data$Species <- as.character(data$Species)
str(data)
data[c(30,50,70), 'Species'] <- 'tiger'
data[c(31,51,71), 'Sepal.Length'] <- 99.9
boxplot(data$Sepal.Length)
data <- data[data$Sepal.Length<20,]
table(data$Species) # 카운트 해서 출력
data$Species <- ifelse(data$Species=='setosa' | data$Species=='versicolor' | data$Species=='virginica', data$Species, NA)
table(data$Species) # 결측치는 카운트 X
data
summary(data)
data <- data[!is.na(data$Species),]
data


# 과제(data: mpg)
data <- as.data.frame(ggplot2::mpg) # ggplot2의 mpg로 한정
data[c(10,14,58,93),'drv'] <- 'k'
data[c(29,43,129,203),'cty'] <-c(3,4,39,42)

# 1) drv 이상치 유무를 확인하고 이상치 있는 경우 결측 처리후 결측 데이터 제외
table(data$drv)
data$drv <- ifelse(data$drv=='4' | data$drv=='f' | data$drv=='r', data$drv, NA)
data <- data[!is.na(data$drv),]

# 2) 상자그림을 이용하여 cty에 이상치 유무를 확인하고 정상범위에서 벗어난값은 제외하고 다시 상자그림을 그리시오
boxplot(data$cty)
quantile(data$cty)
data <- data[data$cty<30 & data$cty>4,]
boxplot(data$cty)
