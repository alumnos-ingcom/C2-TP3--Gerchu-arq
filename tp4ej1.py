############################################################
# Matias G. Quevedo - @Gerchu-arq
# Ingreso de números enteros, TP4, Unidad 3.
# UNRN Andina - Introducción a la Ingenieria en Computación
############################################################


# Reemplazar por las funciones del ejercicio
# No esta empezado, aun....

def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero



if __name__ == "__main__":
    ingreso_entero("Ingresar un numero entero:")
