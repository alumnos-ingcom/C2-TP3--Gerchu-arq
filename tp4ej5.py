############################################################
# Matias G. Quevedo - @Gerchu-arq
# 5. Números positivos y negativos, TP4, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################


#Escribir una función que reciba un número e indique si el mismo es positivo, negativo o cero.

def ingreso_numero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except Exception as ex:
# Ha habido una excepción <class 'TypeError'>
        print("Ha habido una excepción", type(ex))
    else:  #Entra en else, no ha ocurrido ninguna excepción
        print("No ha ocurrido ninguna excepción")
        return entero


def signo(numero):
    if numero == 0: print(f'Numero:{numero} Neutro')
    elif numero < 0: print(f'Numero:{numero} Negativo')
    else: return print(f'Numero:{numero} Positivo')
 
 ############ FUNCION PRINCIPAL ####################################
 
if __name__ == "__main__":
    numero = ingreso_numero("Ingresar un numero entero:")
    signo(numero)