#Ingreso por teclado de la cantidad de nombres
cantidad = input("¿Cuantos nombres desea ingresar?: ")

#Chequeamos que sea un numero
while cantidad.isdecimal() == False:
    print("¡Error. Solo numeros!")
    cantidad = input("Ingrese un numero: ")

#Convertimos
cantidad = int(cantidad)

#Arranca la lista vacia
nombres = []

#Variable contador = 0
contador = 0

#Este bucle generara el ingreso de los nombres segun cantidad
while contador < cantidad:
    #Variable name para que sea auxiliar para guardar ingresos
    name = input("Ingrese un nombre: ")
    #el append siempre agrega al final de las listas
    nombres.append(name)
    #variable contador(de vueltas) se usara para comparar con cantidad
    contador = contador + 1

print("*** ATENCION ***")

#Ahora tenemos que pedir el nombre que queremos ver cuantas veces aparece
dato = input("Ingrese nombre para verificar: ")

# Veces sera una variable donde contaremos las veces que aparece ese 'x' nombre
veces = 0

#con el for recorremos la lista nombres (n es la auxiliar del for)
for n in nombres:
    #Este if verifica si hay coincidencia
    if n == dato:
        #incrementamos la variable veces si hay coincidencia
        veces = veces + 1 

#Al terminar el for sabremos si hubo repeticiones

print( dato + " aparece " + str(veces) + " veces")


#NOTA: Al momento de crear la lista verificar todas las posibilidades