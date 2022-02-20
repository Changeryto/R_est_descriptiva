#Fórma rápida
q = 10 + 1i

#En forma binómica
w = complex(real=10, imaginary = 1)

#En forma polar
e = complex(modulus = 10.04988, argument = 1.570796)


q
w
e

#Raíz cuadrada
r = sqrt(as.complex(-1))
r

#Obter la parte real
Re(r)
Re(q)

#Obtener la parte imaginaria
Im(r)
Im(q)

#Obtener el módulo
Mod(r)
Mod(q)

#Orbtener el argumento
Arg(r)
Arg(q)

#Obtener el conjugado
Conj(r)


(3 + 2i)*4
(3+2i)/(-1+2i)
2 + 5i #Error: 2 + 5*i

#pi + sqrt(2)i Error
complex(real=pi, imaginary = sqrt(2)) -> w
w
#R nos dá la raiz cuadrada con la parte real positiva
sqrt(as.complex(-5)) 
#Para obtener la parte real negativa
-1*sqrt(as.complex(-5)) 

sqrt(3 + 2i)
exp(3 + 2i)
sin(3 + 2i)
cos(3 + 2i)

#Módulo = sqrt(Re(z)^2 + Im(z)^2)
Mod(w)

#Argumento = arctan(Im(z)/Re(z))
# = arcos(Re(z)/Mod(z))
# = arcsin(Im(z))/Mod(z)
#Va en el intervalo (-pi, pi])
Arg(w)
Arg(-1+0i)
Arg(-1-2i)
#Conjugado = Re(z) - Im(z)i
Conj(w)

### z = Mod(z) * (cos(Arg(z)) + sin(Arg(z)i)
complex(modulus = 2, argument = pi/2) -> z2
Mod(z2)
Arg(z2)
pi/2
