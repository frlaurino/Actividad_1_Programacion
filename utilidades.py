def calcular_ancho_texto(socios, columna, encabezado):
    ancho = len(encabezado)
    for i in range(len(socios)):
        if len(str(socios[i][columna])) > ancho:
            ancho = len(str(socios[i][columna]))
    return ancho + 3

def completar_espacios(texto, ancho):
    cantidad_espacios = ancho - len(str(texto))
    texto_con_espacios = str(texto) + " " * cantidad_espacios
    return texto_con_espacios

def mostrar_registros(socios):
    ancho_numero = calcular_ancho_texto(socios, 0, "Nro. Socio")
    ancho_nombre = calcular_ancho_texto(socios, 1, "Nombre")
    ancho_apellido = calcular_ancho_texto(socios, 2, "Apellido")
    ancho_actividad = calcular_ancho_texto(socios, 3, "Actividad")
    ancho_cuota = calcular_ancho_texto(socios, 4, "Cuota")
    ancho_estado = calcular_ancho_texto(socios, 5, "Estado")

    print()
    print(completar_espacios("Nro. Socio", ancho_numero), end="")
    print(completar_espacios("Nombre", ancho_nombre), end="")
    print(completar_espacios("Apellido", ancho_apellido), end="")
    print(completar_espacios("Actividad", ancho_actividad), end="")
    print(completar_espacios("Cuota", ancho_cuota), end="")
    print(completar_espacios("Estado", ancho_estado))

    for i in range(len(socios)):
        print(completar_espacios(socios[i][0], ancho_numero), end="")
        print(completar_espacios(socios[i][1], ancho_nombre), end="")
        print(completar_espacios(socios[i][2], ancho_apellido), end="")
        print(completar_espacios(socios[i][3], ancho_actividad), end="")
        print(completar_espacios(socios[i][4], ancho_cuota), end="")
        print(completar_espacios(socios[i][5], ancho_estado))

def filtrar_por_categoria(socios, categoria):
    socios_filtrados = []
    for i in range(len(socios)):
        if socios[i][3] == categoria:
            socios_filtrados.append(socios[i])
    return socios_filtrados

