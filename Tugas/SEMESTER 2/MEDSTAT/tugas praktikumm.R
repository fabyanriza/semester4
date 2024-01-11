setwd("D:/Materi/SEMESTER 2/Medstat/Kumpulan data")
data1 = read.csv("possum.csv", header = TRUE) # Memanggil data
data1

## MENGGUNAKAN FUNGSI BAWAAN R
# Membandingkan variabel umur dengan panjang total possum
x = data1$footlgth # variable yang diambil adalah panjang kaki posum(variabel independen/prediktor)
y = data1$earconch # Variabel yang diambil adalah telinga posum(variable dependen/respons)

plot(x,y) # Menampilkan scatter plot dari variabel telinga dan panjang kaki

hasil <- lm(y ~ x, data = data1) # Mencari hasil dengan rumus regresi
summary(hasil) # Menampilkan hasil dari perhitungan regresi

## MENGGUNAKAN CARA MANUAL

slope = function(x,y){
  mean_x = mean(x)
  mean_y = mean(y)
  sxy = sum((x - mean_x)*(y - mean_y))
  sxx = sum((x - mean_x)^2)
  b1 = sxy / sxx
  return (b1)
}

intercept <- function(x, y, b1){
  b0 <- mean(y) - (b1 * mean(x))
  return(b0)
}

b1 <- slope(x, y)
b0 <- intercept(x, y, b1)
# pembuatan model 
model = lm(y~x, data=data1)
summary(model)

model$coefficients
summary(model)$r.squared
predict(model, data.frame(x = 50))

