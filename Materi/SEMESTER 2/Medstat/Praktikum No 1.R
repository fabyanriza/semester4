setwd("D:/Materi/Medstat")


Data1=read.table("M2-Data Praktikum 1.txt", header=TRUE,
colClasses = c("numeric", "factor")) #Mengambil data
y1=Data1$Asam_Askorbat  
perlakuan=Data1$Varietas  #assign variable
summary(Data1) #summary data


#ANOVA
ANOVA1 <- aov(y1 ~ perlakuan, data = Data1)
summary(ANOVA1)

#Dikarenakan p value < alpha, maka kita tolak hipotesis 0, dan disimpulkan bahwa paling tidak terdapat perbedaan kandungan asam askorbat diantara 3 sampel(variasi). 
