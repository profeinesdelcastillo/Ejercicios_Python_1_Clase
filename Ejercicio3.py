
def conversion(segundos):
    minutos = int(segundos / 60)
    horas = int(minutos / 60)
    minutos_resto = minutos - (horas*60) 
    segundos_resto = segundos - (horas*60*60) - (minutos_resto *60)
    if horas<10:
        horast = "0" + str(horas)
    else:
        horast = str(horas)
    if minutos_resto < 10:
        minutost = "0" + str(minutos_resto)
    else:
        minutost = str(minutos_resto)
    if segundos_resto < 10:
        segundost = "0" + str(segundos_resto)
    else:
        segundost = str(segundos_resto)

    return(horast + ":" + minutost + ":" + segundost)

#####################################################

print(conversion(1000))