from validaciones import validar_rango


# Muestra las opciones y devuelve una opcion ya validada entre 1 y 8
def mostrar_menu():
    print()
    print("=== SISTEMA DE GESTION - GIMNASIO ===")
    print("1 - Dar de alta un socio")
    print("2 - Consultar un socio")
    print("3 - Modificar un socio")
    print("4 - Eliminar un socio")
    print("5 - Mostrar todos los socios")
    print("6 - Consultar socios por actividad")
    print("7 - Ver estadisticas")
    print("8 - Salir")
    print()

    opcion = validar_rango(1, 8)
    return opcion
