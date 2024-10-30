personas = ["Susana","Tamara","Ana","Susana","Susana","Tomas","Ana"]

ingresos = {}

for n in personas:
    if n not in ingresos:
        ingresos[n] = 1
    else:
        ingresos[n] += 1

print(ingresos)
