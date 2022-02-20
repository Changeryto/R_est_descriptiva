#De la tarea 1

#Problema 1
minutos = 250000000 / 60
horas = minutos / 60
dias = horas / 24
dias

#año2018: 
dias = dias - 365
anios = 1
#2019
dias = dias -365
anios = anios +1
#2020
dias = dias -366
anios = anios +1
#2021
dias = dias - 365
anios = anios +1
#2021
dias = dias - 365
anios = anios +1
#2022
dias = dias - 365
anios = anios +1
#2023
dias =dias - 365
anios = anios +1
full = anios + (dias/366)
print(paste(sprintf("Son %f años y %f dias, es decir %f años para llegar a 250 mds", anios, dias, full)))

año = 2018 + anios

#Meses
#enero
dias = dias -31
meses = 1
#febrero
dias = dias - 29
meses = meses + 1
#marzo
dias = dias - 31
meses = meses +1
#abril
dias = dias - 30 
meses = meses + 1
#mayo
dias = dias -31
meses = meses + 1
#junio
dias = dias - 30
meses = meses + 1
#julio
dias = dias - 31
meses = meses +1
#agosto
dias = dias - 31
meses = meses +1
#septiemre
dias = dias -30
meses = meses +1
#octubre
dias = dias - 31
meses = meses +1
#noviembre
dias = dias -30
meses = meses +1
mes = meses +1

#Al quedarnos 2 dias estamos en el 2 de diciembre
dia = floor(dias)
#Hora
hora = (dias-2) * 24
minuto = (hora-12)*60
h = floor(hora)
m = floor(minuto)

#Respuesta

print(paste(sprintf("Fecha: %f / %f / %f a las %f : %f ", dia, mes, año, h, m)), )




#Problema 2

grado1 = function(A, B, C){
  x = (C - B) / A
}


r = grado1(2,4,0)
r

primera = grado1(5, 3, 0)
primera
segunda = grado1(7, 4, 18)
segunda
tercera = grado1(1, 1, 1)
tercera

#Problema 3
res = (3*exp(1) - pi)
print(res, 4)

num = ((2 + 3i)^2) / (5 + 8i)
print(num, 4)

print(Mod(num), 5)

