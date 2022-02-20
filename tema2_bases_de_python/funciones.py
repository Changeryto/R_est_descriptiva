#Todos los métodos son funciones, pero no todas las funciones son métodos
'''
def suma(x, y):
    return x + y

nueva_suma = suma(10, 5)
print(nueva_suma)

class Operaciones:
    def __init__(self):
        self.resultado = None
    def suma(self, x, y):
        self.resultado = x + y
        return self.resultado
    @staticmethod
    def suma_estatica(x, y):
        return (x + y)
    
objeto_suma =Operaciones()
print(objeto_suma.suma(2, 30))

print(Operaciones.suma_estatica(10, 5))

'''
'''
def BuscaPares(rango):
    regresar = ""
    for n in range(rango):
        if n % 2 == 0:
            regresar += "\n" + str(n)
    return regresar
            
            
x = BuscaPares(int(input("Rango: ")))

print(x)
'''

def SumaResta(a, b):
    suma = a + b
    resta = a - b
    return "Suma: " + str(suma) + ", Resta: " + str(resta)

y = SumaResta(10, 5)
print(y)