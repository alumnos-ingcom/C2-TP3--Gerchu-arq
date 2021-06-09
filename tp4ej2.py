############################################################
# Matias G. Quevedo - @Gerchu-arq
# 2. Suma Lenta, TP4, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################

'''Escribir una función que haga la suma entre dos números enteros sin hacer
la operación de manera directa. Esto quiere decir que para hacer la suma entre
4 y 3, las operaciones resultantes deberán ser 4+1+1+1.
La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.'''

from tp4ej5 import ingreso_numero  # uso la funcion ingreso_numero(mensaje) del ej. 5
 

def suma_lenta(numero, otro_numero):
    for i in range(abs(otro_numero)):
        
        
def prueba():
    numero = ingreso_numero("Ingresar numero:")
    otro_numero = ingreso_numero("Ingresar otro numero:")
    suma_lenta(numero, otro_numero)   

if __name__ == "__main__":
    prueba()
