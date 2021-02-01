# ������ ����
a<-c(1,2,3,4)
b<-c(5,6,7,8)
c<-a+b
c
c<-a*b

# ���̰� �ٸ� ���Ϳ���(���ͱ��� ���ι��) => ª�� ���Ͱ� �ݺ��Ǿ� ���
b<-c(5,6)
c<-a+b
c<-a*b

# ���̰� �ٸ� ���Ϳ���(���ͱ��� ���ι��X) => ��� �޽��� + ���
a<-c(1,2,3,4)
b<-c(5,6,7)
c<-a+b
c<-a*b

# ������������ : ���͵��� ������ ����
id<-c('f1','f2','f3','f4')
name<-c('������','�Ѻ�','����','��')
age<-c(10,20,30,40)
isBoy<-c(T,T,F,F)


# ������������ �����Լ�
df<-data.frame(id,name,age,isBoy,stringsAsFactors = T)
df
str(df)

# ����������
df[2,3]           # 2�� 3��
df[c(2,3),]       # 2��,3�� ��翭
df[c(2,3),c(2,4)] # 2��,3��, 2��,4��
df[,c(2,4)]       # �����, 2��,4��
df[c('name','age')]

# ���� ����
df$age
df$name
df$name[3:4]

# ����������
data()
iris

# ����������
write.csv(iris,file='iris.csv')
write.csv(iris,file='iris.csv',row.names=F)
write.csv(df,file='df.csv')

# ������ �б�
data<-read.csv('df.csv')
data

# ���� ������ �б�
install.packages("readxl")
library(readxl)
a<-read_excel('test.xlsx')
a
a1<-read_excel('test.xlsx', sheet=2)
a1
a2<-read_excel('test.xlsx', sheet="Sheet2")
a2

# Ŭ�����忡 �ִ� ���� ��������
a3<-read.table("clipboard")
a3
a3<-read.table("clipboard", header = T)
a3
iris
str(iris)
nrow(iris)  # �� ��
ncol(iris)  # �� ��
head(iris,3)
tail(iris)
min(iris$Sepal.Length)        # �ּҰ�
quantile(iris$Sepal.Length)   # ���������
max(iris$Sepal.Length)        # �ִ밪
summary(iris)
View(iris)

# subset(������������, ����, [��ȸ�ϰ� ������])
subset(iris,Sepal.Length>6)
subset(iris,Sepal.Length>6, c(1,5))
subset(iris,Sepal.Length>6, c('Sepal.Length','Species'))
subset(iris,Sepal.Length>6 | Sepal.Width>=3.5, c('Sepal.Length','Sepal.Width','Species'))
subset(iris,Sepal.Length>6 & Sepal.Width>=3.5, c('Sepal.Length','Sepal.Width','Species'))

# ���� ������ setosa �� ���� ������ ���
summary(subset(iris, Species=='setosa'))
summary(iris[iris$Species=='setosa',])
str(iris[iris$Species=='setosa',c('Sepal.Length')])            # ����
str(iris[iris$Species=='setosa',c('Sepal.Length','Species')])  # ������������

# dplyr ����Ű
install.packages('dplyr')
library(dplyr)
data<-iris
data

# �÷��� ����
# rename(������������, ��������1=������1...)
data <- rename(data, len1=Sepal.Length, wid1=Sepal.Width)
head(data)

# �� �÷� ����
data$length <- data$len1 + data$Petal.Length
head(data)

# ifelse(����,���ΰ��, �����ΰ��)
data$new <- ifelse(data$len1>5, 'good','low')
head(data)
data$new2 <- ifelse(data$len1>5, 'good', ifelse(data$len1>4.5, 'low', 'fail'))
head(data)
View(data)

# dplyr ��Ű���� �Լ���
# %>% ���������� �ո��ɾ��� ����� �޸��ɾ��� �Է����� ó��
# rename : �÷��� ����
# filter(����) : ���ǿ� �´� ������ ����
# select(���̸�1,���̸�2...) : �������� �� ����
# arrange(�÷���) : ����
data8 <- head(data,10) %>% filter(new=='good')
data8 %>% select(Petal.Length, Petal.Width)
data8
head(iris,10) %>% filter(Sepal.Length>=5) %>% 
  select(Sepal.Length, Species) %>% arrange(desc(Sepal.Length))

# mutate(����1=����1, ����2=����2, ...) : �����߰�
head(iris) %>% mutate(hap=Sepal.Length+Petal.Length, 
                      avg=(Sepal.Width+Petal.Width)/2,
                      grade=ifelse(Sepal.Width>=3.5, 'good','poor')
                      )
# summarise() : ���
# group_by(�÷���) 
head(iris) %>% summarise(avg=mean(Sepal.Length))
iris %>% group_by(Species) %>% summarise(avg=mean(Sepal.Length))


# ����
install.packages("ggplot2")
library(ggplot2)
View(mpg)

data <- mpg
head(data)
# 1) �ڵ�������ȸ�翡 ���� ���ÿ����� ������
data %>% group_by(manufacturer) %>% summarise(avg=mean(cty))
# 2) cty, hwy�� ��տ��񺯼��� �߰�
data$avg <- (data$cty+data$hwy)/2
# 3) ��տ��� ���� ������ 3�� ���
head(data %>% arrange(desc(avg)), 3)  



