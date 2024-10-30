#Ingreso por teclado de la cantidad de nombres
cantidad = input("¿Cuantos nombres desea ingresar?: ")

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
	
print(nombres)

