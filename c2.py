import math
# -b +- r(b²-4.a.c)
#       /2
def bahaskara(a, b, c):
    paso1 = 0
    try:
        paso1 = math.sqrt(pow(b,2)-(4*a*c))
        print(paso1)
        x1 = (-b + paso1)/(2*a)
        x2 = (-b - paso1)/(2*a)
        print(x1)
        print(x2)
    except ValueError:
        print('No existe la raiz cuadrada de un numero negativo.')

a = float(input('Ingrese el primer termino: '))
b = float(input('Ingrese el segundo termino: '))
c = float(input('Ingrese el tercer termino: '))
bahaskara(a,b,c)
