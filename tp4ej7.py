############################################################
# Matias G. Quevedo - @Gerchu-arq
# 7. Restas sucesivas, TP4, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################


'''Escribir una función que mediante restas sucesivas, obtenga el valor del cociente
y resto de dos números enteros.'''

from tp4ej5 import ingreso_numero  # uso la funcion ingreso_numero(mensaje) del ej. 5


def division_lenta(dividendo, divisor):
    if (divisor == 0) : print("Error, division por cero \n")
    elif (dividendo < divisor):
        cociente = 0; residuo = 0;
        print(f'El cociente es:{cociente} y el resto es:{residuo}')
    else:
        cociente = 0; residuo = 0
        while(residuo >= 0):
            if(dividendo - divisor < 0): break
            else:
                residuo = dividendo - divisor
                cociente = cociente + 1
                dividendo = residuo
        print(f'El cociente es:{cociente} y el resto es:{residuo}')

def prueba():
    dividendo = ingreso_numero("Ingresar dividendo:")
    divisor = ingreso_numero("Ingresar divisor:")
    division_lenta(dividendo, divisor)   

 ############ FUNCION PRINCIPAL ####################################
 
if __name__ == "__main__":
    prueba()         
