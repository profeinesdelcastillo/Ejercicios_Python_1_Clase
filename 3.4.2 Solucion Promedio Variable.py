
# Si se desea para hacer la suma se puede usar la funcion built-in sum() 
# de esa manera evitas el uso del for 

def promedio_variable(*args):
    suma = 0
    for n in args:
        suma += n
    promedio = suma / len(args)
    return promedio


#############################


print(promedio_variable(10,8,9))
print(promedio_variable(6,6,9,9))