2 * (3 + 5/2)

2 * ((3 + 5)/2)

2 / 3 + 5

2%/%3 + 5

2^3 +5

2^-4


725 %/% 7

725 %% 7


# D = d * q + r
# r = D - (d * q)
# q = D %/% d
# r = D %% d
725 - 103*7

pi

2 * pi

3 ^pi

pi^2

#Infinitos
Inf

-Inf

NA #Valor desconocido


NaN #No es un número

0/0

2 ^50

2 ^-15


c(2^30,2^-15, 1, 2, 3/2) #Vector
#Se expresarán en notación si 2 o más
#están en la misma

#Raíz cuadrada
sqrt(pi)

#Exponente de 'e'
exp(1)

#Logaritmo natural
log(6)

#Logaritmo base 10
log10(0.056)

#Logaritmo de base variable 
#La base es el segundo número
log(5, 10)

#Absoluto
abs(-1.2)


#Factorial (4 * 3 * 2 * 1)
factorial(4)
factorial(10)

#Combinación elementos C tamaño
#elementos arriba tamaño abajo en el binomio de Newton
choose(5, 3) #Número de subconjuntos de 3 otenibles de un conjunto de 5

choose(10, 1)

choose(1, 1)
choose(10, 4)


#Funciones trigonométricas
#En radianes (rad = grados * pi / 180)

#Seno
sin(pi/2) #Seno de 90 grados

cos(pi / 3)

#Seno pi
sinpi(1/2) # = sin(pi * 1/2)

#Tangente
tan(2)

tan(pi) # -1.224647e-16 ~ -Inf
tan(pi/2) # +1.224647e-16 ~ Inf

#Arcoseno sólo entre -1 y 1
asin(0.8660254) #arc sin en radianes
asin(0.8660254) * 180 / pi #arc sin en grados


#Arcocoseno sólo entre -1 y 1
acos(-0.9)

#Arcotangente
atan(2)

#Visitar trigonometría de wikipedia


#Números en coma fflotante

#Especificar las cifras significativas del número x
print(sqrt(2), 5)

#Redondear a las cifras decimales
round(sqrt(2), 5)


sqrt(2)
floor(sqrt(2)) #Se redondea a la baja
ceiling((sqrt(2)))#Se redondea a la alza

trunc(sqrt(2)) #Se trunca


#Ejemplo
sqrt(2)^2-2 #Casi cero
#Ten cuidado al hacer operaciones paulatinas


2^50
print(2^50, 2)

#R no puede trabajar con garantía con más de 16 cifras decimales
print(pi, 16)
print(pi,20) #Me va a dar las cifras posibles
print(pi, 23) #Da un error

round(sqrt(2), 4)^2
#No es igual a
sqrt(2)^2


#R redondea en caso de empate al valor a la cifra par
round(1.255, 2) #Excepto en 2 decenas
round(1.355,2)
round(1.455,2)
round(1.655, 2)
round(1.735,2)

#De no especificar el segundo número de round(x,n)
#n se considera 0


#Para especificar de forma explícita:
round(digits = 5, sqrt(2))
#Igual a
round(sqrt(2), 5)

#Presiona TAB para desplegar los parámetros solicitados
log(x = 12, base = 10)
