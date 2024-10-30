# Ejercicio 1.
numeros = [1, 2, 3, 4, 5, 6]
suma = 0

# Evitar sumar el último número de la lista.
for n in numeros[:-1]:
    suma = suma + n

print(suma)