from datos import socios, actividades, estados
from menu import mostrar_menu
from crud import alta_socio, consultar_socio, modificar_socio, eliminar_socio
from utilidades import mostrar_registros
from consultas import consultar_por_categoria
from estadisticas import mostrar_estadisticas


opcion = 0

while opcion != 8:
    opcion = mostrar_menu()

    if opcion == 1:
        alta_socio(socios, actividades)
    elif opcion == 2:
        consultar_socio(socios)
    elif opcion == 3:
        modificar_socio(socios, actividades, estados)
    elif opcion == 4:
        eliminar_socio(socios)
    elif opcion == 5:
        mostrar_registros(socios)
    elif opcion == 6:
        consultar_por_categoria(socios, actividades)
    elif opcion == 7:
        mostrar_estadisticas(socios, actividades)

print("saliendo del sistema.")
