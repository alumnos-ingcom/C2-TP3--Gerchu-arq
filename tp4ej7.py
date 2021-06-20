############################################################
# Matias G. Quevedo - @Gerchu-arq
# 7. Restas sucesivas, TP4, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################


'''Escribir una función que mediante restas sucesivas, obtenga el valor del cociente
y resto de dos números enteros.'''



from tp4ej1 import ingreso_numero  


def division_lenta(dividendo, divisor):
    lista = []
    if (dividendo < divisor):
        cociente = 0; residuo = 0;
    else:
        cociente = 0; residuo = 0
        while(residuo >= 0):
            if(dividendo - divisor < 0): break
            else:
                residuo = dividendo - divisor
                cociente = cociente + 1
                dividendo = residuo
    lista.append(cociente)
    lista.append(residuo)
    return lista

def prueba():
    dividendo = ingreso_numero("Ingresar dividendo:")
    try:
        divisor = ingreso_numero("Ingresar divisor:")
    except:
        divisor = 0
    if divisor == 0:
        print("error en la division")
        # sale del programa
        exit()
    else:
        rta_division = division_lenta(dividendo, divisor)
        print(f'\n El cociente y el resto es:')
        return rta_division
    
 ############ FUNCION PRINCIPAL ####################################
 
if __name__ == "__main__":
    print(prueba())         
