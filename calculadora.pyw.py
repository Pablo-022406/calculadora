import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import Canvas, Radiobutton
from PIL import ImageTk, Image
from tkinter import ANCHOR, NW
from math import sin, cos, tan


def init_window(): 
    window = tk.Tk()
    window.title('Mi primera aplicacion')
    window.geometry('400x250')
    label = tk.Label(window, text='Calculadora', font=('Arial bold', 15))
    label.grid(column=0, row=0)

    entrada1 = tk.Entry(window, width=10)
    entrada2 = tk.Entry(window, width=10)

    
    entrada1.grid(column=1, row=1)
    entrada2.grid(column=1, row=2)

    label_entrada1 = tk.Label(window, text='Ingrese primer numero:', font=('Arial bold', 10))
    label_entrada1.grid(column=0, row=1)
    label_entrada2 = tk.Label(window, text='Ingrese segundo numero:', font=('Arial bold', 10))    
    label_entrada2.grid(column=0, row=2)

    label_operador = tk.Label(window, text='Escoja un operador',font=('Arial bold', 10))
    label_operador.grid(column=0,row=3)

    combo_operadores = ttk.Combobox(window)
    combo_operadores['values'] = ['+', '-', '*', '/', 'pow']
    combo_operadores.current(0)
    combo_operadores.grid(column=1, row=3)

    label_resultado = tk.Label(window, text='Resultado: ', font=('Arial bold',15))
    label_resultado.grid(column=0, row=5)
    boton = tk.Button(window, command = lambda: click_calcular(label_resultado,
                                                entrada1.get(), entrada2.get(),
                                                combo_operadores.get()),
                                                text="Calcular", 
                                                bg="purple", 
                                                fg="white")
    boton.grid(column=1, row=4)
    def calculadora(num1, num2, operador):
        if operador =='+':
            resultado = num1 + num2           
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            resultado = round(num1 / num2, 2)       
        else:
            resultado = num1 ** num2
        return resultado

    def click_calcular(label1, num1, num2, operador):
        valor1 = float(num1)
        valor2 = float(num2)

        res = calculadora(valor1, valor2, operador)

        label_resultado.configure(text='Resultado: '+ str(res))     
    def sinWindow():
        newWindow = tk.Toplevel(window)
        newWindow.geometry('1100x500')
        canvas = Canvas(newWindow, width = 923, height = 317)
        img = ImageTk.PhotoImage(Image.open("identidades.png")) 
        canvas.create_image(0,0,anchor=NW,image=img)
        canvas.image = img   
        entry = tk.Entry(newWindow, width=10)
        label_operacion = tk.Label(newWindow)
        def selec(num,op):
            n = int(num)
            res = 0
            if op=='sin':
                res = sin(n)
            elif op=='cos':
                res = cos(n)
            elif op=='tan':
                res = tan(n)
            res_final = str(res)
            label_operacion.configure(text=''+res_final)                 
        boton_sin = tk.Button(newWindow, text="Seno", command=lambda : selec(entry.get(), 'sin'))
        boton_sin.grid(column=0, row=2)
        boton_cos = tk.Button(newWindow, text='Coseno',command=lambda : selec(entry.get(), 'cos'))
        boton_cos.grid(column=0, row=3)
        boton_tan = tk.Button(newWindow, text='Tangente',command=lambda : selec(entry.get(), 'tan'))
        boton_tan.grid(column=0, row=4)

        canvas.grid(column=0, row=0)   
        entry.grid(column=0, row=1)
        label_operacion.grid(column=0, row=5)
    boton_sin = tk.Button(window, text="Operaciones trigonometricas", command=sinWindow)
    boton_sin.grid(column=0, row=6)

    window.mainloop()

init_window()








