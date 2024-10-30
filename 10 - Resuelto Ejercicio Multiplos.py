

inicio = input("Ingrese el numero de incio del rango: ")
inicio = int(inicio)

final = input("Ingrese el numero del final del rango: ")
final = int(final)

multiplos = []

for n in range(inicio,final+1,1):
	if n%3 == 0 and n%5 == 0:
		multiplos.append(n)

print("Los multiplos de 3 y de 5 en ese rango son: ")
print(multiplos)
