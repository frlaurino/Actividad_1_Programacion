from validaciones import solicitar_categoria
from utilidades import filtrar_por_categoria, mostrar_registros


def consultar_por_categoria(socios, actividades):
    print("CONSULTA DE SOCIOS POR ACTIVIDAD")

    categoria = solicitar_categoria("Seleccione una actividad:", actividades)

    socios_filtrados = filtrar_por_categoria(socios, categoria)

    print("Socios de la actividad", categoria)

    if len(socios_filtrados) > 0:
        mostrar_registros(socios_filtrados)
    else:
        print("No hay socios en esta actividad.")