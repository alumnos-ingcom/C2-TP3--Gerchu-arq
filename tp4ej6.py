############################################################
# Matias G. Quevedo - @Gerchu-arq
# 6. Maximo y minimo, TP4, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################

from tp4ej1 import ingreso_numero  


def Cargar_Lista(n):
    i = 1
    lista=[]
    while n >= i:
        nro = ingreso_numero("Ingresar un numero entero: ")
        lista.append(nro)
        i = i + 1    
    return lista

def Minimo(lista):
    min = lista[0]
    for x in range(0,len(lista)):
        if lista[x] <= min:
            min = lista[x]
    return min
        
def Maximo(lista):
    max = lista[0]
    for x in range(0,len(lista)):
        if lista[x] >= max:
            max = lista[x]
    return max

def prueba():
    
    n = ingreso_numero("Ingresar cantidad de nros.:")
    Lista = Cargar_Lista(n)
    print(f"\n {Lista}")     
    print(f"\nMinimo:{Minimo(Lista)} y Maximo:{Maximo(Lista)}")
 
############ FUNCION PRINCIPAL ####################################
 
if __name__ == "__main__":
    prueba()      
    
    
    
