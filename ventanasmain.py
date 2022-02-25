#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk  # Importar
from tkinter import *
from tkinter.ttk import *
from math import sqrt


# -----------------------------------------------------------------------------------------------------------------------
def primos():
    def solucionPrimos():
        primo = int(txtboxPrimo.get())
        numero = range(2, primo)
        contador = 0
        for n in numero:
            if primo % n == 0:
                contador += 1
        if contador > 0:
            messagebox.showinfo("Calcular Primo", "El numero ingresado NO es primo")
        else:
            messagebox.showinfo("Calcular Primo", "El numero ingresado SI es primo")

    ventanaPrimos = tk.Tk()  # Definir ventana
    ventanaPrimos.title("Calcular Numero Primo")  # titulo de la ventana
    ventanaPrimos.geometry('500x500')  # Ancho por alto
    ventanaPrimos.configure(background='snow')  # color de fondo de la ventana
    # text: texto que dirá el label, bg:color del fondo del label, fg: color del texto
    # padx=e o pady=e, son para dejar espacio entre objetos, en donde la e es una constante.
    lblCalculoPrimos = tk.Label(ventanaPrimos, text="Calcular Numeros Primos", bg="turquoise", fg="black")
    lblCalculoPrimos.pack(pady=40)
    lblDigiteNumero = tk.Label(ventanaPrimos, text="Digite el numero que desea saber si es primo: ", bg="turquoise",
                               fg="black")
    lblDigiteNumero.pack(pady=15)
    txtboxPrimo = tk.Entry(ventanaPrimos)
    txtboxPrimo.pack()
    btnCalcular = tk.Button(ventanaPrimos, text="CALCULAR", bg="azure", fg="black", command=solucionPrimos)
    btnCalcular.pack(pady=15)
    ventanaPrimos.mainloop()


# -----------------------------------------------------------------------------------------------------------------------
def fibonacci():
    def f(n):
        return ((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))

    lista = []

    def solucionFibonacci():
        endNumber = int(txtboxFibonacci.get()) + 1
        n = 0
        cur = f(n)
        while cur <= endNumber:
            if 0 <= cur:
                enteros = int(cur)
                lista.append(enteros)
            n += 1
            cur = f(n)
        messagebox.showinfo("Calcular Secuencia Fibonacci", lista)

    ventanaFibonacci = tk.Tk()  # Definir ventana
    ventanaFibonacci.title("Calcular Secuencia Fibonacci")  # titulo de la ventana
    ventanaFibonacci.geometry('500x500')  # Ancho por alto
    ventanaFibonacci.configure(background='snow')  # color de fondo de la ventana
    # text: texto que dirá el label, bg:color del fondo del label, fg: color del texto
    # padx=e o pady=e, son para dejar espacio entre objetos, en donde la e es una constante.
    lblCalculoFibonacci1 = tk.Label(ventanaFibonacci, text="Calcular Secuencia Fibonacci", bg="turquoise",
                                    fg="black")
    lblCalculoFibonacci1.pack(pady=40)
    lblCalculoFibonacci2 = tk.Label(ventanaFibonacci, text="Recuerde que el cálculo de le secuencia empezará desde 0",
                                    bg="turquoise", fg="black")
    lblCalculoFibonacci2.pack(pady=15)
    lblDigiteNumero = tk.Label(ventanaFibonacci, text="¿Hasta que número desea calcular la secuencia fibonacci?: ",
                               bg="turquoise", fg="black")
    lblDigiteNumero.pack(pady=15)
    txtboxFibonacci = tk.Entry(ventanaFibonacci)
    txtboxFibonacci.pack()
    btnCalcular = tk.Button(ventanaFibonacci, text="CALCULAR", bg="azure", fg="black", command=solucionFibonacci)
    btnCalcular.pack(pady=15)
    ventanaFibonacci.mainloop()


# -----------------------------------------------------------------------------------------------------------------------
def bases():
    def BaseaBase():
        numConv = int(txtboxNumeroConv.get())
        baseIni = int(txtboxBaseInicial.get())
        baseFinal = int(txtboxBaseFinal.get())
        paso1 = ChibiBases.convertirbaseadecimal(numConv, baseIni)
        final = ChibiBases.convertirdecimalabase(paso1, baseFinal)
        messagebox.showinfo("El Número convertido es: ", final)

    ventanaBaseaBase = tk.Tk()  # Definir ventana
    ventanaBaseaBase.title("Cambiar Numero de Base")  # titulo de la ventana
    ventanaBaseaBase.geometry('500x500')  # Ancho por alto
    ventanaBaseaBase.configure(background='snow')  # color de fondo de la ventana
    # text: texto que dirá el label, bg:color del fondo del label, fg: color del texto
    # padx=e o pady=e, son para dejar espacio entre objetos, en donde la e es una constante.
    lblCalculoBaseaBase = tk.Label(ventanaBaseaBase, text="Cambiar Numero de Base", bg="turquoise", fg="black")
    lblCalculoBaseaBase.pack(pady=40)
    lblDigiteNumero1 = tk.Label(ventanaBaseaBase, text="Digite que base tiene el numero a convertir: ",
                                bg="turquoise", fg="black")
    lblDigiteNumero1.pack(pady=15)
    txtboxBaseInicial = tk.Entry(ventanaBaseaBase)
    txtboxBaseInicial.pack()
    lblDigiteNumero2 = tk.Label(ventanaBaseaBase, text="Digite el Número a convertir: ", bg="turquoise", fg="black")
    lblDigiteNumero2.pack(pady=15)
    txtboxNumeroConv = tk.Entry(ventanaBaseaBase)
    txtboxNumeroConv.pack()
    lblDigiteNumero3 = tk.Label(ventanaBaseaBase, text="Digite la base a la que quiere convertir el numero: ",
                                bg="turquoise", fg="black")
    lblDigiteNumero3.pack(pady=15)
    txtboxBaseFinal = tk.Entry(ventanaBaseaBase)
    txtboxBaseFinal.pack()
    btnCalcular = tk.Button(ventanaBaseaBase, text="CALCULAR", bg="azure", fg="black", command=BaseaBase)
    btnCalcular.pack(pady=15)
    ventanaBaseaBase.mainloop()


# -----------------------------------------------------------------------------------------------------------------------
ventanaOpciones = tk.Tk()  # Definir ventana
ventanaOpciones.title("Main")  # titulo de la ventana
ventanaOpciones.geometry('500x400')  # Ancho por alto
ventanaOpciones.configure(background='snow')  # color de fondo de la ventana
# text: texto que dirá el label, bg:color del fondo del label, fg: color del texto
# padx=e o pady=e, son para dejar espacio entre objetos, en donde la e es una constante.
lblOpciones = tk.Label(ventanaOpciones, text="¿QUE DESEA CALCULAR?", bg="turquoise", fg="black")
lblOpciones.pack(pady=30)
btnCalcular1 = tk.Button(ventanaOpciones, text="FIBONACCI", bg="black", fg="white", command=fibonacci)
btnCalcular1.pack(pady=15)
btnCalcular2 = tk.Button(ventanaOpciones, text="PRIMOS", bg="black", fg="white", command=primos)
btnCalcular2.pack(pady=15)
btnCalcular3 = tk.Button(ventanaOpciones, text="BASES", bg="black", fg="white", command=bases)
btnCalcular3.pack(pady=15)
ventanaOpciones.mainloop()


# In[ ]:





# In[ ]:




