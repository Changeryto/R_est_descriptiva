#Variables:
#nombre_varaible = valor
#Funciones:
#nombre_función = function(variable) {función}

miVariable = 4

x = (pi^2)/2
2 - miVariable
sqrt(x*2)

#Flecha valor para asignar variables (igual que con el igual, la verdad)

y <- cos(pi/4)
y

sin(pi/4) + cos(pi/4) -> z

z

#No se puede usar un operador no numérico para un operador binario
#edad <- str(30) + "años"

#Entre comillas para declararlo como string
Nombre = "Rubén Téllez" 
#String signfica cadena de texto

pi.4 <- 4 * pi

pi.4 / 4




#Funcones

nombre_funcion = function(variable_pedida1){2*x}

nombre_funcion(10)

doble = function(x){2*x}
doble(15)

##Función f(x) = x^3 - (3^x) * sen(x)
f = function(x){x^3 - 3^x * sin(x)}

f(0.2)
f(pi/2)

#Recomendación, identar
uwu = function(x){
  2*x + 3*x + 4*x
  }

uwu(10)

#La nomencltura de fecha se mantiene

division_al_cuadrado_del_divisor <- function(x, y){
  (x / y) ^ y
}

division_al_cuadrado_del_divisor(5, 7)

g <- function(x, y, z){
  exp(x* y * z)
}

g(0.00002,0.00004,0.00006)

p <- function(numero){
  retorno = 0;
  retorno = retorno + numero;
  retorno = retorno + numero;
  retorno = retorno + numero;
  uwu(retorno)
}

p(5)

#Método ls() regresa una lista con los valores
#y funciones cargados
ls()

#El método rm() borra desde el script
#una valor o función en memoria

rm(uwu)

#Borrar todo elemento desde el script
rm(list = ls())
