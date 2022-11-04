# Calculadora basica de python

# Importo todo del modulo tkinter
from tkinter import *

# Declaro una variable que usare como expresion
expresion = ""

def press(num):
    global expresion
    expresion = expresion + str(num)
    equation.set(expresion)

# Funcion que evaluara la formula
def equalpress():
    # Hacemos uso de try except para manejar errores como division entre cero, etc
    try:
        global expresion
        # la funcion eval evaluara la formula y la funcion str convertira el resultado en string
        total = str(eval(expresion))
        equation.set(total)
        # inicializamos la expresion como un string vacio
        expresion=""
    except:
        equation.set(" error ")
        expresion=""

def clear():
    global expresion
    expresion=""
    equation.set("")

# Codigo principal
if __name__ == "__main__":
    # creo la ventana
    gui = Tk()

    # defino un color de fondo para la ventana
    gui.configure(bg="light green")

    # defino un titulo a la ventana
    gui.title("Calculadora Python")

    # defino la resolucion de la ventana
    gui.geometry("336x190")

    # defino un stringvar que usare para la ecuacion
    equation = StringVar()

    # creo una caja de texto donde mostrare la expresion
    campo_expresion = Entry(gui, textvariable=equation)

    campo_expresion.grid(columnspan=4, ipadx=70)

    # creo la rejilla de numeros
    b0 = Button(gui, text="0", fg='black', command=lambda: press(0), height=1, width=7)
    b0.grid(row=2, column=0)

    b1 = Button(gui, text = '1', fg ='black', command=lambda: press(1), height=1, width=7)
    b1.grid(row=2, column=1)

    b2 = Button(gui, text='2', fg ='black', command=lambda: press(2), height=1, width=7)
    b2.grid(row=2, column=2)

    b3 = Button(gui, text='3', fg ='black', command=lambda: press(3), height=1, width=7)
    b3.grid(row=3, column=0)

    b4 = Button(gui, text='4', fg ='black', command=lambda: press(4), height=1, width=7)
    b4.grid(row=3, column=1)

    b5 = Button(gui, text='5', fg ='black', command=lambda: press(5), height=1, width=7)
    b5.grid(row=3, column=2)

    b6 = Button(gui, text='6', fg ='black', command=lambda: press(6), height=1, width=7)
    b6.grid(row=4, column=0)

    b7 = Button(gui, text='7', fg ='black', command=lambda: press(7), height=1, width=7)
    b7.grid(row=4, column=1)

    b8 = Button(gui, text='8', fg ='black', command=lambda: press(8), height=1, width=7)
    b8.grid(row=4, column=2)

    b9 = Button(gui, text='9', fg ='black', command=lambda: press(9), height=1, width=7)
    b9.grid(row=5, column=0)

    decimal = Button(gui, text='.', fg ='black', command=lambda: press('.'), height=1, width=7)
    decimal.grid(row=6, column=0)

    resta = Button(gui, text='-', fg ='black', command=lambda: press(' - '), height=1, width=7)
    resta.grid(row=3, column=3)

    suma = Button(gui, text='+', fg ='black', command=lambda: press(' + '), height=1, width=7)
    suma.grid(row=2, column=3)

    producto = Button(gui, text='*', fg ='black', command=lambda: press(' * '), height=1, width=7)
    producto.grid(row=4, column=3)

    igual = Button(gui, text='=', fg ='black', command=equalpress, height=1, width=7)
    igual.grid(row=5, column=2)

    limpiar = Button(gui, text='Clear', fg ='black', command=clear, height=1, width=7)
    limpiar.grid(row=5, column=1)

    division = Button(gui, text='/', fg ='black', command=lambda: press(' / '), height=1, width=7)
    division.grid(row=5, column=3)

    gui.mainloop()
