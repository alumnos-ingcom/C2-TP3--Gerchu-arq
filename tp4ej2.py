############################################################
# Matias G. Quevedo - @Gerchu-arq
# 2. Suma Lenta, TP4, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################



'''Escribir una función que haga la suma entre dos números enteros sin hacer la operación
de manera directa. Esto quiere decir que para hacer la suma entre 4 y 3, las operaciones
resultantes deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.'''

from tp4ej5 import ingreso_numero  # uso la funcion ingreso_numero(mensaje) del ej. 5
 

def suma_lenta(numero, otro_numero):
    suma = numero
    for i in range(abs(otro_numero)):
        if otro_numero < 0:
            aux = False
            suma = suma - 1
            unos_neg = (i+1)*"-1"
        else:
            aux = True
            suma = suma + 1
            unos_pos = (i+1)*"+1"
    if aux == False :        
        print(f'{numero}'+ unos_neg)
    else:
        print(f'{numero}'+ unos_pos)
        
    return suma  
        
def prueba():
    numero = ingreso_numero("Ingresar numero:")
    otro_numero = ingreso_numero("Ingresar otro numero:")
    print(f'suma lenta : {suma_lenta(numero, otro_numero) }')

if __name__ == "__main__":
    prueba()
