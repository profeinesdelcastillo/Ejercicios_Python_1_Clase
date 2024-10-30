def fibo(cantidad):
    # Chequear que la cantidad sea un valor válido.
    if cantidad <= 2:
        # Terminar la función.
        return "La cantidad de terminos debe ser mayor que 2"
    # Esta es la lista que vamos a retornar. Por definición empieza
    # con los términos 0 y 1.
    f = [0, 1]
    # Añadir elementos hasta haber alcanzado la cantidad indicada.
    while len(f) < cantidad:
        # Agregamos al final de la lista un elemento que es la suma
        # de los dos anteriores.
        f.append(f[-1] + f[-2])
    return f


print(fibo(1))
print(fibo(10))