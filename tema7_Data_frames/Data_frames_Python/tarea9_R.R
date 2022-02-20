

setwd("C:/Programación ExL/R_y_Python/tema7_Data_frames/Data_frames_Python")

run = read.csv("run.csv")





#1. Indica cuantos estudiantes formaron 
#parte del estudio de deporte

a = length(rownames(run))
sprintf("Hay %i participantes", a)


#2. Indica cuantos individuos 
#son hombres y cuantos son mujeres

b = table(run$genero)
b = data.frame(b)

paste(sprintf("Hombres: %i | Mujeres: %i", b$Freq[1], b$Freq[2]))


#3. Calcula el porcentaje medio de variación del 
#pulso por minuto entre antes y después de hacer 
#ejercicio y compara el valor de los que hacen 
#ejercicio habitualmente y los que no. 
#¿Observas mucha diferencia?


run$vr = run$pulso.despues-run$pulso.antes
c = aggregate(vr~ hace.deporte,data = run, FUN = mean)
c = data.frame(c)
sprintf("No hace deporte: %f | Hace deporte: %f", c$vr[1], c$vr[2])


#4. Calcula el porcentaje medio de variación del 
#pulso por minuto entre antes y después de hacer 
#ejercicio  para los estudiantes que 
#hacen ejercicio habitualmente y compara el 
#valor de los hombres con el de las mujeres. 
#¿Observas mucha diferencia?

H = run[which(run$genero=="H"),]
M = run[which(run$genero=="M"),]
d_h = aggregate(vr ~ hace.deporte, data = H, FUN = mean)
d_h = data.frame(d_h)
d_m = aggregate(vr ~ hace.deporte, data = M, FUN = mean)
d_m = data.frame(d_m)

sprintf("Hombres: No hacen deporte %f | Hacen deporte %f", d_h$vr[1], d_h$vr[2])
sprintf("Mujeres: No hacen deporte %f | Hacen deporte %f", d_m$vr[1], d_m$vr[2])



#5. Calcula el porcentaje medio de variación del 
#pulso por minuto entre antes y después de hacer 
#ejercicio para los estudiantes que no hacen 
#ejercicio habitualmente y compara el valor de los 
#fumadores con los no fumadores. 
#¿Observas mucha diferencia?

e = aggregate(vr ~ fuma, data = run, FUN = mean)
e = data.frame(e)
sprintf("No fuma: %f | Fuma: %f", e$vr[1], e$vr[2])



#6. Calcula el porcentaje medio de variación del 
#pulso por minuto entre antes y después de hacer 
#ejercicio de todos los estudiantes según el tipo 
#de actividad física que realizan.
#¿Observas alguna diferencia?

f = aggregate(vr ~ tipo.actividad, data = run, FUN = mean)
f = data.frame(f)
count = 0
f_s = c()
for(tip in length(f$tipo.actividad)){
  count = count + 1
  f_s = c(f_s, sprintf("Tipo de actividad: %s: %f", f$tipo.actividad[tip], f$vr[count]))
}
f_s





















