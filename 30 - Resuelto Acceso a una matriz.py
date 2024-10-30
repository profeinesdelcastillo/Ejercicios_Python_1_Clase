

matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]

print(matriz)

fila = int(input("Fila: "))
columna = int(input("Columna: "))



if fila < len(matriz):
	if columna < len(matriz[fila]):
		print(matriz[fila][columna])
	else:
		print("Error en las columnas")
else:
	print("Error en las filas")
