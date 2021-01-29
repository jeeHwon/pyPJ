# 주석
# 실행 ctrl + enter
# 콘솔지우기 ctrl + l
a<-100
b<-20
c<-'spring'
c<-"winter"

# 벡터함수 c(), 모두 같은 데이터 타입
v1 = c(1,2,3,4,5)
str(v1) # str : 정보확인 
v2 = c('one','two','three')
str(v2)
length(v1)  # 벡터길이 확인
length(v2)

v1<-seq(1,100,by=2)
v1<-c(1,'hi',3.14, TRUE)# string으로 인식
v2<-c(T,F,TRUE,FALSE)   # bool
v1<-c(1,3.14,5.0,-999)  # 숫자
min(v1)
max(v1)
median(v1)
sum(v1)

#NaN: 숫자로 표현될수 없는 값, Inf(무한대)
v1<-c(2/2,-2/2,1/0,0/0)
str(v1)
mode(v1) # 데이터 타입

# 데이터 형변환 as.xxxx()
v1<-c(-1,3,3.14,0,100,-100)
v1<-as.logical(v1)  # 0:FALSE / !0: TRUE
v1<-as.numeric(v1)
v1<-as.character(v1)
v1<-c('spring','summer','autumn','winter')
nchar(v1) # 문자개수 출력

# 슬라이싱
substr('123456789',2,5) # 2번째부터 5번째까지 슬라이싱
substr(v1,1,2)

# 자르기
# strsplit : 지정된 문자를 기준으로 나누어 벡터로 변환
s='2021-01-28'
s2=strsplit(s,'-')
s2

# 문자열 합치기
paste("one","two","three","four")
paste("one","two","three","four",sep="-")
  
# 대소문자 변환
toupper("AbcdeFgHi")
tolower("AbcdeFgHi")
f<-c('사과','딸기','사과','포도','복숭아')  

# factor() : 범주형 데이터
fruit<-factor(f)
f
fruit
mode(f)     # character
mode(fruit) # numeric : 내부적으로 숫자로된 코드값 벡터가 구성
str(f)
str(fruit)

#levels 순서변경 : 그래프, 분석결과 출력시 영향
fruit2<-factor(f,levels=c('포도','사과','딸기','복숭아')) 
fruit2
  
# 항목간에 서열이 존재하는 경우
grade<-c('수','우','수','양','가','우','가','미','양','미')
g2<-factor(grade, ordered = T)
g2
g3<-factor(grade,levels=c('가','양','미','우','수'))  
g3
  
#숫자벡터를 factor로 변환
n<-c(30,10,10,20,20,30,10)
n1<-factor(n)
n1
n

# 요소접근
v1<-c(10,20,30,40,50,60,70,80,90,100)
v1
v1[3]
v1[c(1,3,5,7,9)]  # v1벡터의 1,3,5,7,9번째 요소 선택
v1[c(9,7,5,3,1)]  # 출력순서 변경

# 연속된 숫자벡터 생성
v1<-31:40
v1
v1<-51:100
v1
v1[15:35] #15~35 요소 출력
# seq(from=시작값, to=종료값, by=증감값)
v1 = seq(10,20,2)
v1
v1 = seq(100,20,-3)
v1

# 불린추출
v1[3]
idx<-c(T,F)
v1[idx]
v1>50
v1[v1>50]
v1[1]<-1000
v1[v1<50]<-0
v1

# v1 벡터의 모든 값을 1로 변경
v1<-1 # 바뀌지 않고 할당돼
v1
v1<-c(9,8,7,6,5)
length(v1)
v1[1:length(v1)]<-1
v1

v1<-c(1,2,3,4,5)
v1<-c(0,v1)     # v1 앞에 0추가
v1<-c(-2,-1,v1) # v1 앞에 -2, -1 추가
v1<-c(v1,6)     # v1 뒤에 6추가
v1<-c(v1,c(7,8))# v1 뒤에 7, 8추가

# 벡터합치기
v1<-c(1,2,3)
v2<-c(4,5,6)
v3<-c(7,8,9)
v<-c(v1,v2,v3)
v1<-c('a','b','c','f','g')
v2<-c('d','e')

# append(원본벡터,추가벡터,추가할위치)
v1<-append(v1,v2,3)
# v1의 1,3,5,7번째 데이터 출력
v1[c(1,3,5,7)]
# v1의 1,3,5,7번째 제외한 데이터 출력
v1[-c(1,3,5,7)]
# v1의 마지막 데이터 출력
length(v1)
v1[length(v1)]
# v1의 마지막 데이터를 제외한 출력
v1[-length(v1)]
lidx<-c(T,T,F,F,F,F,F)
v1[lidx]

# 논리벡터에는 ! 사용
v1[!lidx]

# 과제
# 10의 학생의 수학점수 변수에 데이터 저장
score<-c(98,76,85,68,76,85,99,87,54,76)
# 전체의 평균, 최소값, 최대값, 중간값 출력
mean(score)
min(score)
max(score)
median(score)


