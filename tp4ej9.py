############################################################
# Matias G. Quevedo - @Gerchu-arq
# 9. Números primos, TP4, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################

#Escribir una función que indique con True si un numero indicado es Primo.

from tp4ej5 import ingreso_numero  # uso la funcion ingreso_numero(mensaje) del ej. 5

def es_primo(numero):
    numero = abs(numero)
    for n in range(2, numero):
        if numero % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True

def prueba():
     numero = ingreso_numero("Ingresar un numero:")
     es_primo(numero)
############ FUNCION PRINCIPAL ####################################
 
if __name__ == "__main__":
    prueba()
   
