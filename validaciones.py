# Devuelve el num > 0
def validar_positivo(mensaje):
    print(mensaje, end="")
    valor = int(input())

    while valor <= 0:
        print("El valor debe ser mayor a 0:", end=" ")
        valor = int(input())
    
    return valor

# Devuelve el num si esta en el rango
def validar_rango(minimo,maximo):
    print("Ingrese un numero entre", minimo, "y", maximo, end=": ")
    valor = int(input())

    while valor < minimo or valor > maximo:
        print("El valor debe estar comprendido entre", minimo, "y", maximo)
        print("Ingrese un numero entre", minimo, "y", maximo, end=": ")
        valor=int(input())

    return valor

# Devuelve el texto si no es vacio
def validar_texto(mensaje):
    texto = input(mensaje)

    while texto == "":
        print("El valor no puede estar vacio")
        texto = input(mensaje)

    return texto

# Devuelve la categoria elegida
def solicitar_categoria(titulo, categorias):
    print(titulo)
    largo = len(categorias)
 
    for i in range(largo):
        print(i + 1, "-", categorias[i])
 
    opcion = validar_rango(1, largo)
 
    return categorias[opcion - 1]

# Devuelve True si el numero de socio existe
def existe_socio(socios, numero):
    encontrado = False
    pos = 0
 
    while pos < len(socios) and not encontrado:
        if socios[pos][0] == numero:
            encontrado = True
        else:
            pos += 1
 
    return encontrado

# Valida si el codigo del nuevo socio que se quiere anotar ya existe
def solicitar_cod_nuevo(socios, mensaje):
    numero = validar_positivo(mensaje)

    while existe_socio(socios, numero):
        print("El numero de socio", numero, "ya existe")
        numero = validar_positivo(mensaje)
    
    return numero