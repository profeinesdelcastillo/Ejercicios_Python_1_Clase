def verificar(texto):
    while texto == "":
        print("Error")
        texto = input("Ingrese nuevamente: ")
    return texto


def convertir(dato):
    while dato.isdecimal() == False:
        print("¡Error!")
        dato = input("Ingrese nuevamente: ")
    return int(dato)



################################

personas = {}

while True:
    print("Menú:")
    print("1 - Agregar")
    print("2 - Mostrar el más chico")
    print("3 - Mostrar el más grande")
    print("4 - Salir")
    opcion = input(">>> ")
    if opcion == "1":
        nombre = input("Ingrese un nombre: ")
        nombre = verificar(nombre)
        edad = input("Ingrese una edad: ")
        edad = convertir(edad)
        personas[nombre] = edad
        print("¡Se agrego una persona!")
    elif opcion == "2":
        # El 'truco' consiste en poner el 200 para 
        # que arranque aux_edad con un número grande 
        # y siempre tome el primero del diccionario.
        aux_edad = 200 
        # aux_nombre la dejamos vacio
        aux_nombre = ""
        for n in personas:
            if personas[n] < aux_edad:
                aux_edad = personas[n]
                aux_nombre = n
        print(aux_nombre +" es la persona más chica")
    elif opcion == "3":
        # El 'truco' consiste en poner el 0 para 
        # que arranque aux_edad con cero
        # y siempre tome el primero del diccionario.
        aux_edad = 0
        # aux_nombre la dejamos vacio
        aux_nombre = ""
        for n in personas:
            if personas[n] > aux_edad:
                aux_edad = personas[n]
                aux_nombre = n
        print(aux_nombre +" es la persona más grande")
    elif opcion == "4":
        print("¡Gracias por utilizar el programa!")
        break
    else:
        print("¡Error de opción!")

