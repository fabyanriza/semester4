
#MEMANGGIL DATA
Data3=read.table("M2-Data Praktikum 3.txt", header=TRUE,
colClasses = c("numeric", "factor", "factor"))
y3=Data3$Hardness
Treatments=Data3$Tip
Block=Data3$Block
summary(Data3)

#ANOVA
ANOVA3 <- aov(y3 ~ Treatments + Block, data = Data3)
summary(ANOVA3)
