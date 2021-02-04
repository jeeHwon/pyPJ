# 3
library(ggplot2)
data <- mpg
data$total <- (data$cty+data$hwy)/2
data

# 4-1
library(dplyr)
data<-iris
dim(data)
str(data)
summary(data)

# 4-2
plot(data$Petal.Length, data$Petal.Width, pch=20, cex=2, col='#CB230C')

# 4-3
cor(data$Petal.Length, data$Petal.Width)
cor.test(data$Petal.Length, data$Petal.Width, method = "pearson", conf.level = 0.95) 
t.test(data$Petal.Length, data$Petal.Width, var.equal = T)
