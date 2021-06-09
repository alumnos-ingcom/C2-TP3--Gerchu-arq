############################################################
# Matias G. Quevedo - @Gerchu-arq
# 3. Conversión de temperaturas, TP4, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################

'''Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.
Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit como un
número real, utilice esta formula para calcular los grados centígrados y retorne el resultado
obtenido. Y viceversa.'''


def convertir_a_centigrados(fahrenheit):

    '''convierte temperatura en grados fahrenheit a grados celsius'''

    centigrados = (fahrenheit -32 ) * 5.0/9.0
    print(f'{fahrenheit:.2f} grados Fahrenheit son {centigrados:.2f} grados Celsius')

def convertir_a_fahrenheit(centigrados):

    '''convierte temperatura en grados celsius a fahrenheit'''

    fahrenheit = 9.0/5.0 * centigrados +32
    print(f'{centigrados:.2f} grados Celsius son {fahrenheit:.2f} grados Fahrenheit')

'''while True:
    print('1.- Fahrenheit a Celsius')
    print('2.- Celsius a Fahrenheit')

    try:
        opcion = int(input('Seleccione una opción: '))
        if opcion == 1:
            print(fahrenheit_celsius())
        elif opcion == 2:
            print(celsius_fahrenheit())
        elif opcion == 3:
            print('Hasta luego')
        else:
            raise ValueError
    except ValueError:
        print('Ingrese solo números.(1/2)')'''

if __name__ == "__main__":
    fahrenheit = int(input('Ingrese la temperatura en grados Fahrenheit: '))
    centigrados = int(input('Ingrese la temperatura en grados Celsius: '))
    convertir_a_centigrados(fahrenheit)
    convertir_a_fahrenheit(centigrados)
    
    


