""" LICENCIA

ChibiBases, Libreria para Python3 que permite convertir bases numericas
    Copyright (C) 2017  David Melara

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

# Zona Para Definiciones De Funciones

# ---------------------------------------------------#

# Esta funcion convierte un numero entero decimal a cualquier base


def convertirdecimalabase(_numero, _base):  # Funcion Recibe numero decimal y la base que se desea formato int

    numeroconvertido = ""            # Variable para guardar el numero convertido

    _numero = int(_numero)           # Convertir numero en entero

    _base = int(_base)               # Convertir base en entero

    while True:                      # Repetir infinitamente

        _residuo = _numero % _base   # Variable para guardar el residuo del mod

        _numero -= _residuo          # Restamos residuo al numero original

        if _residuo >= 10:           # Si es mayor a 10 (A = 10)

            _residuo += 55           # Sumamos 55 para el respectivo ASCII decimal (A = 65 y Z = 90)

            numeroconvertido += str(chr(int(_residuo))) # Convertimos residuo en su Caracter ASCII y
                                                        # lo añadimos a la cadena del numero convertido
        else:

            numeroconvertido += str(int(_residuo))   # Si es menor a 10 añadir
                                                     # el residuo directamente
        _numero = _numero / _base    # Numero para a ser el resultado de numero / base

        if _numero == 0:       # Si ya dividimos lo mas posible entonces

            break              # Romper para salir del While

    numeroconvertido = numeroconvertido[::-1]  # Le damos vuelta al
                                               # numero convertido (se lee de izquierda a derecha)
    return numeroconvertido     #Regresamos el numero convertido

# fin de la funcion


def convertirbaseadecimal(_numero, _base):  # Funcion recibe _numero en cadena y base original en int

    numeroconvertido = 0   # Variable para guardar el numero convertido

    _numero = str(_numero)  # Convertir numero en entero

    _base = int(_base)      # Convertir base en entero

    _numero = _numero[::-1] # Damos vuelta al numero para multiplicar por su potencia

    for i in range(0, len(_numero), 1):  # Contamos potencia "i" desde 0 hasta maxima posicion numero

        if ord(_numero[i]) >= 65:  # Si el caracter ASCII es (A=65) o mayor, convertilo a numero

            numeroconvertido += int(ord(_numero[i]) - 55) * pow(_base, i)  # Restamos 55 para convertir Letra en Numero

        else:

            numeroconvertido += int(ord(_numero[i]) - 48) * pow(_base, i); # Convertimos numero asci en numero int
                                                                           # Multiplicamos numero por la base
                                                                           # elevada a la posicion, y lo suma a
                                                                           # la variable numeroconvertido
    return numeroconvertido  # Retornamos el numero convertido en formato int

# Zona De Algoritmos----------------------------------------------------

"""

print("Decimal 210 a distintas bases:")

print("Binario: " + convertirdecimalabase(210, 2))

print("Octal: " + convertirdecimalabase(210, 8))

print("Hexadecimal: " + convertirdecimalabase(210, 16))

print("Base 32: " + convertirdecimalabase(210, 32))

print("")

print("Binario 11010010 es: " + str(convertirbaseadecimal("11010010", 2)))

print("Octal 322 es: " + str(convertirbaseadecimal("322", 8)))

print("Hexadecimal D2 es: " + str(convertirbaseadecimal("D2", 16)))

print("Base32 6I es: " + str(convertirbaseadecimal("6I", 32)))

"""
