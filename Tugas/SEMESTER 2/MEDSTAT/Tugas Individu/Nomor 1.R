setwd("D:/Tugas/SEMESTER 2/MEDSTAT/Tugas Individu")

Data_1 <- read.csv("D:/Tugas/SEMESTER 2/MEDSTAT/Tugas Individu/Data_1.csv", sep=";")

Peringkat=Data_1$Peringkat_Sensorik

summary(Data_1)


ANOVA1 <- aov(Peringkat ~ Perlakuan, data = Data_1)
summary(ANOVA1)
