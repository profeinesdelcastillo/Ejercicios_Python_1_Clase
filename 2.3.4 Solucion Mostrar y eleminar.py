# Ejercicio 2.
numeros = [1, 2, 3, 4, 5, 6]
print(numeros)

while len(numeros) > 0:
    # Imprimir el primer elemento.
    print(numeros[0])
    # Eliminarlo.
    del numeros[0]

#confirmamos que quedo vacia la lista
print(numeros)