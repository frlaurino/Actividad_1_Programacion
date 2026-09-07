from utilidades import filtrar_por_categoria
from validaciones import solicitar_categoria

def cantidad_socios(socios):
    return len(socios)


def cantidad_por_actividad(socios, categoria):
    cant_socios_filtrados = len(filtrar_por_categoria(socios, categoria))
    return cant_socios_filtrados


def promedio_cuotas(socios):
    suma = 0

    if cantidad_socios(socios) > 0:
        for i in range(len(socios)):
            suma = suma + socios[i][4]
        promedio = suma / cantidad_socios(socios)
    else:
        promedio = 0
        
    return promedio

def mostrar_estadisticas(socios, actividades):
    total = cantidad_socios(socios)
    categoria = solicitar_categoria("Seleccione una actividad:", actividades)
    cantidad_actividad = cantidad_por_actividad(socios, categoria)
    promedio = promedio_cuotas(socios)

    print("ESTADISTICAS")
    print("Cantidad total de socios:", total)
    print("Cantidad de socios de la actividad", categoria + ":", cantidad_actividad)
    print("Promedio de cuota:", promedio)