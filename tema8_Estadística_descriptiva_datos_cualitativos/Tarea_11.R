
alumnos = c("M","H","H","M","M","H")

edades = sample(x = 10:15,
                size = 10,
                replace = TRUE)

edad = sample(x = 18:20,
                size = 10,
                replace = TRUE)

altura = sample(x = 150:200,
                size = 10,
                replace = TRUE)

peso = sample(x = 50:100,
              size = 10,
              replace = TRUE)


#Da la instrucción que defina la tabla de 
#frecuencias absolutas de un vector llamado 
#alumnos.

table(alumnos)


#Con una sola instrucción, define la tabla 
#de frecuencias relativas de un vector 
#llamado edades.

prop.table(table(edades))

#Con una sola instrucción, define la tabla 
#bidimensional conjunta de frecuencias 
#absolutas de dos vectores llamados altura 
#y peso, de forma que las filas correspondan a
#altura y las columnas a peso.

table(altura, peso)

#Con una sola instrucción, define la tabla 
#bidimensional conjunta de frecuencias 
#relativas calculadas dentro del total, 
#de dos vectores llamados edad y altura, 
#de forma que las filas correspondan a 
#altura y las columnas a edad.

prop.table(
  table(
    altura, edad
  )
)



#Con una sola instrucción, 
#dibuja un diagrama de barras básico 
#de un vector llamado edad.

barplot(table(edad), legend.text = TRUE)


#Con una sola instrucción, dibuja un 
#diagrama circular básico de un vector 
#llamado alumnos.

pie(table(alumnos))


#La tabla DNase es uno de los data 
#frames que tiene predefinidos R. 
#Da la instrucción que dibuje un diagrama 
#de barras básico de la variable density de 
#este mismo data frame.

barplot(
  table(DNase$density)
)
