install.packages("foreign")
library(foreign)
data<-read.spss(file='data/Koweps_hpc10_2015_beta1.sav',to.data.frame = T)

#2016년 복지패널데이터
data
nrow(data)
ncol(data)

# 변수명 변경 : rename(data, 새변수명 = 예전변수명,..)
library("dplyr")
data <- rename(data, 
               gender = h10_g3,
               birth = h10_g4,
               marriage = h10_g10,
               religion =	h10_g11,
               code_job = h10_eco9,
               income = p1002_8aq1,
               code_region = h10_reg7)

# 절차 : 변수검토 및 전처리 -> 변수간 관계분석
# 성별에 따른 급여차이
data               
mode(data$gender)
table(data$gender)

# 이상치 결측처리
data$gender <- ifelse(data$gender !=1 & data$gender != 2, NA, data$gender)
table(data$gender)
table(is.na(data$gender))
barplot(table(data$gender))
data$gender2 <- ifelse(data$gender ==1 , '남자', '여자')
barplot(table(data$gender2))

mode(data$income)
summary(data$income)
data$income <- ifelse(data$income >= 1 & data$income <= 9998, data$income, NA)
summary(data$income)
gender_income <- data %>% filter(!is.na(income))
hist(gender_income$income)
boxplot(gender_income$income)
gender_income2 <- gender_income %>% group_by(gender2) %>% summarise(avgincome=mean(income))
gender_income2

#ggplot2
# 데이터,축 +그래프종류 + 기타설정
library(ggplot2)
ggplot(data=gender_income2, aes(x=gender2, y=avgincome)) + geom_col()
ggplot(data=gender_income2, aes(x=gender2, y=avgincome)) + geom_col() + ylim(0,500)

# 나이와 급여의 관계
mode(data$birth)
summary(data$birth)
table(is.na(data$birth))
data$age <- 2015 -data$birth+1
summary(data$age)
hist(data$age)
age_income <- data%>% filter(!is.na(income)) %>% group_by(age) %>% summarise(avgincome=mean(income))
age_income
ggplot(data=age_income, aes(x=age, y=avgincome))+geom_line()

# 연령대별 급여차이
data <- data %>% mutate(ageg=ifelse(age<30,'초년',ifelse(age<60,'중년','노년')))
mode(data$ageg)
table(data$ageg)
barplot(table(data$ageg))
ageg_income <- data %>% filter(!is.na(income)) %>% group_by(ageg) %>% summarise(avgincome=mean(income))
ageg_income
ggplot(data=ageg_income, aes(x=ageg, y=avgincome)) + geom_col() + scale_x_discrete(limits=c('초년','중년','노년'))

# 연령대, 성별별 급여차이
ageg_gender_income <- data %>% filter(!is.na(income)) %>% group_by(ageg, gender2) %>% summarise(avgincome = mean(income))
ageg_gender_income
ageg_gender_income
ggplot(data=ageg_gender_income, aes(x=ageg, y=avgincome, fill=gender2)) + geom_col() + scale_x_discrete(limits=c('초년','중년','노년'))

# 나이, 성별별 급여차이
age_gender_income <- data %>% filter(!is.na(income)) %>% group_by(age, gender2) %>% summarise(avgincome=mean(income))
head(age_gender_income)
ggplot(data=age_gender_income, aes(x=age, y=avgincome, col=gender2)) + geom_line()


# 직업별 급여차이
mode(data$code_job)
table(data$code_job)
library(readxl)
joblist <- read_excel('data/Koweps_Codebook.xlsx', sheet=2)
head(joblist)
data <- left_join(data, joblist, id="code_job")
job_income <- data %>% filter(!is.na(income)) %>% group_by(job) %>% summarise(avgincome=mean(income))
job_income

# 급여를 많이 받는 직종 10개
top10 <- job_income %>% arrange(desc(avgincome)) %>% head(10)
top10
ggplot(data=top10, aes(x=job, y=avgincome)) + geom_col()

# 가로막대 회전
ggplot(data=top10, aes(x=job, y=avgincome)) + geom_col() + coord_flip()

# 성별별 직업빈도
womanjob <- data %>% filter(!is.na(job) & gender2=='여자')%>% group_by(job) %>% summarise(cnt=n())
womanjob %>% arrange(desc(cnt))
ggplot(data=womanjob, aes(x=job, y=cnt)) + geom_col() + coord_flip()

# 지역별 연령대 비율
regionlist = data.frame(code_region=c(1:7), region=c("서울", "수도권(인천/경기)","부산/경남/울산","대구/경북","대전/충남",
                                        "강원/충북","광주/전남/전북/제주도"))
regionlist
data <- left_join(data, regionlist, id="code_region")
region_ageg_rate <- data %>% group_by(region, ageg) %>% summarise(cnt=n()) %>% mutate(hap=sum(cnt)) %>% mutate(pct = cnt/hap*100)
region_ageg_rate
ggplot(data=region_ageg_rate, aes(x=region, y=pct, fill=ageg)) + geom_col() + coord_flip()
