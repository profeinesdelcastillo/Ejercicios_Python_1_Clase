sueldo_total = 300 * 1 + 500 * 0 + 700 * 0
sueldo_promedio = sueldo_total / 12

print("El sueldo promedio es:",sueldo_promedio)

if sueldo_promedio < 300:
    print("Sueldo Bajo")
elif sueldo_promedio < 900:
    print("Sueldo Normal")
else:
    print("Sueldo mejor de lo Normal")
