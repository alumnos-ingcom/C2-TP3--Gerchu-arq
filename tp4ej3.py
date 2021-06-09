############################################################
# Matias G. Quevedo - @Gerchu-arq
# 3. Conversión de temperaturas, TP4, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################

'''Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.
Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit como un
número real, utilice esta formula para calcular los grados centígrados y retorne el resultado
obtenido. Y viceversa.'''

from tp4ej5 import ingreso_numero 

def convertir_a_centigrados(fahrenheit):

    '''convierte temperatura en grados fahrenheit a grados celsius'''

    centigrados = (fahrenheit -32 ) * 5.0/9.0
    print(f'{fahrenheit:.2f} grados Fahrenheit son {centigrados:.2f} grados Celsius')

def convertir_a_fahrenheit(centigrados):

    '''convierte temperatura en grados celsius a fahrenheit'''

    fahrenheit = 9.0/5.0 * centigrados +32
    print(f'{centigrados:.2f} grados Celsius son {fahrenheit:.2f} grados Fahrenheit')

def prueba():
    fahrenheit = ingreso_numero('Ingrese la temperatura en grados Fahrenheit: ')
    centigrados = ingreso_numero('Ingrese la temperatura en grados Celsius: ')
    convertir_a_centigrados(fahrenheit)
    convertir_a_fahrenheit(centigrados)
    
if __name__ == "__main__":
    prueba()
    
    


