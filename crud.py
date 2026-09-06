from validaciones import validar_positivo, validar_texto, solicitar_categoria, solicitar_cod_nuevo


# Busca un socio por su numero y devuelve la posicion. Si no existe, devuelve -1
def buscar_socio(socios, numero):
    pos = 0
    encontrado = False
    posicion = -1
    while pos < len(socios) and not encontrado:
        if socios[pos][0] == numero:
            encontrado = True
            posicion = pos
        else:
            pos += 1
    return posicion


# Da de alta un nuevo socio y lo agrega a la matriz
def alta_socio(socios, actividades):
    print("ALTA DE SOCIO")
    numero = solicitar_cod_nuevo(socios, "Ingrese el numero de socio: ")
    nombre = validar_texto("Nombre: ")
    apellido = validar_texto("Apellido: ")
    actividad = solicitar_categoria("Seleccione la actividad:", actividades)
    cuota = validar_positivo("Cuota: ")
    estado = "Activo"
    socio = [numero, nombre, apellido, actividad, cuota, estado]
    socios.append(socio)
    print("Socio cargado con exito. Numero asignado:", numero)


# Busca un socio por numero y muestra todos sus datos
def consultar_socio(socios):
    print("CONSULTA DE SOCIO")
    numero = validar_positivo("Ingrese el numero de socio: ")
    posicion = buscar_socio(socios, numero)
    if posicion == -1:
        print("El numero de socio", numero, "no ha sido encontrado.")
    else:
        socio = socios[posicion]
        print("Numero:", socio[0])
        print("Nombre y Apellido:", socio[1], socio[2])
        print("Actividad:", socio[3])
        print("Cuota:", socio[4])
        print("Estado:", socio[5])


# Localiza un socio y permite modificar sus datos. Nombre y apellido pueden
# conservarse presionando Enter; actividad, cuota y estado se vuelven a pedir
def modificar_socio(socios, actividades, estados):
    print("MODIFICACION DE SOCIO")
    numero = validar_positivo("Ingrese el numero de socio: ")
    posicion = buscar_socio(socios, numero)
    if posicion == -1:
        print("El numero de socio", numero, "no ha sido encontrado.")
    else:
        print("Socio encontrado.")
        print("Presione Enter para conservar nombre y apellido.")
        nombre = input("Nombre [ " + socios[posicion][1] + " ]: ")
        if nombre == "":
            nombre = socios[posicion][1]
        apellido = input("Apellido [ " + socios[posicion][2] + " ]: ")
        if apellido == "":
            apellido = socios[posicion][2]
        actividad = solicitar_categoria("Seleccione la actividad:", actividades)
        cuota = validar_positivo("Cuota: ")
        estado = solicitar_categoria("Seleccione el estado:", estados)
        socios[posicion][1] = nombre
        socios[posicion][2] = apellido
        socios[posicion][3] = actividad
        socios[posicion][4] = cuota
        socios[posicion][5] = estado
        print("Socio modificado correctamente.")


# Localiza un socio, muestra sus datos principales y elimina el registro
# de la matriz previa confirmacion del usuario
def eliminar_socio(socios):
    print("ELIMINACION DE SOCIO")
    numero = validar_positivo("Ingrese el numero de socio: ")
    posicion = buscar_socio(socios, numero)
    if posicion == -1:
        print("El numero de socio", numero, "no ha sido encontrado.")
    else:
        print("Socio encontrado:")
        print(socios[posicion][0], socios[posicion][1], socios[posicion][2])
        confirmacion = input("Confirma la eliminacion? S/N: ")
        if confirmacion == "S" or confirmacion == "s":
            socios.pop(posicion)
            print("Socio eliminado correctamente.")
        else:
            print("Operacion cancelada.")
