#load data
library(haven)
Panel101 <- read_dta("C:/Users/James/Downloads/Panel101.dta")
View(Panel101)

library(dplyr)
library(tidyverse)
library(magrittr)


library(plm)
Panel101<-pdata.frame(Panel101,c("country","year")) #setting panel data

library(ggplot2)

Panel101 %>% 
  ggplot()+
  geom_point(aes(x=x1,y=y,color=country))


model<-y~x1
#dummy 
fixed.dum <-lm(y ~ x1 + factor(country) - 1, data=Panel101) # k-1
summary(fixed.dum)


#1 用plm跑，結果一致
pool <- plm(y ~ x1, data=Panel101, index=c("country", "year"), model="pooling") #pool regression
summary(pool)

#2
fe1<-plm(model, data=Panel101, model='within', effect='individual')
summary(fe1)

fixef(fe1)
#3
re1<-plm(model, data=Panel101, model='random')
summary(re1)

#4 Breusch-Pagan Lagrange Multiplier
plmtest(pool, type=c("bp"))

#5 hauusman
phtest(fe1,re1)


