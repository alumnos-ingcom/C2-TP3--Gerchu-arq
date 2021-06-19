############################################################
# Matias G. Quevedo - @Gerchu-arq
# 4. Comparación de números, TP4, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################

'''Escribir una función que reciba dos valores y retorne:

Retornar -1 si el primero es menor que el segundo. 
Retornar 0 si son iguales.
Retornar 1 si el primero es mayor que el segundo'''

from tp4ej5 import ingreso_numero 

def compara(numero, otro_numero):
    if numero == otro_numero: return 0
    elif numero < otro_numero: return -1
    else: return 1
    
def prueba():
    numero = ingreso_numero("Ingresar un numero entero:")
    otro_numero = ingreso_numero("Ingresar otro numero entero:")
    print(f"Salida: {compara(numero, otro_numero)}")
     
 ############ FUNCION PRINCIPAL ####################################
 
if __name__ == "__main__":
   prueba()
