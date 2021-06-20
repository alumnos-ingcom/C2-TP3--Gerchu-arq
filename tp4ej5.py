############################################################
# Matias G. Quevedo - @Gerchu-arq
# 5. Números positivos y negativos, TP4, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################

from tp4ej1 import ingreso_numero  # uso la funcion ingreso_numero(mensaje) 

#Escribir una función que reciba un número e indique si el mismo es positivo, negativo o cero.


def signo(numero):
    if numero == 0: print(f'Numero:{numero} Neutro')
    elif numero < 0: print(f'Numero:{numero} Negativo')
    else: return print(f'Numero:{numero} Positivo')
<<<<<<< HEAD

def prueba():
     numero = ingreso_numero("Ingresar un numero entero:")
     signo(numero)
 
 ############ FUNCION PRINCIPAL ####################################
 
if __name__ == "__main__":
    prueba()
=======
    
def prueba():
     numero = ingreso_numero("Ingresar un numero entero:")
     signo(numero)
     
 ############ FUNCION PRINCIPAL ####################################
 
if __name__ == "__main__":
   prueba()
>>>>>>> aa34b32d13ff49ce81b8259186dd58fe4c39de13
