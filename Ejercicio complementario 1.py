rol = input("Ingrese su rol: ")
if rol == "admin" or rol == "profesor":
	clave = input("Ingrese clave: ")
	if clave == "1234":
		nombre = input("Ingrese su nombre: ")
		if nombre == "":
			print("¡Error, nombre vacio!")
		else:
			print("Hola, " + nombre)
	else:
		print("¡Clave incorrecta!")
else:
	print("¡Ese rol no existe!")
