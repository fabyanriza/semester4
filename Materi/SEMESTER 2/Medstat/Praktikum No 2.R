Data2=read.table("M2-Data Praktikum 2.txt", header=TRUE,
colClasses = c("numeric", "factor", "factor"))
y2=Data2$Pertumbuhan_Tanaman
Perlakuan_A=Data2$Penyiraman
Perlakuan_B=Data2$Penyinaran_Matahari
summary(Data2)

#ANOVA

#-----------tanpa interaksi-----------
ANOVA2 <- aov(y2 ~ Perlakuan_A + Perlakuan_B, data = Data2)
summary(ANOVA2)


#-----------dengan interaksi-----------
INTERACTION <- aov(y2 ~ Perlakuan_A * Perlakuan_B, data = Data2)
summary(INTERACTION)
