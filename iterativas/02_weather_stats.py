temperature:int
totalTemperature:int = 0
meanTemperature:float = 0

minTemperature:int = 0
maxTemperature:int = 0

countHotDays:int = 0
countColdDays:int = 0

for day in range(1, 8):
    while True:
        try:
            temperature = int(input(f"Indica temperatura del dia {day}: "))
            break
        except ValueError:
            print("Debes escribir un número entero.")

    if temperature > 30:
        countHotDays += 1
    elif temperature < 10:
        countColdDays += 1

    if day == 1:
        minTemperature = temperature
        maxTemperature = temperature
    else:
        if temperature > maxTemperature:
            maxTemperature = temperature

        if temperature < minTemperature:
            minTemperature = temperature

    totalTemperature += temperature

meanTemperature = totalTemperature / 7

if meanTemperature >= 25:
    print(f"La semana fue cálida con una media de {meanTemperature:.2f} ºC")
elif meanTemperature >= 15:
    print(f"La semana fue templada con una media de {meanTemperature:.2f} ºC")
else:
    print(f"La semana fue fría con una media de {meanTemperature:.2f} ºC")

print("La temperatura máxima fue de", maxTemperature, "ºC")
print("La temperatura mínima fue de", minTemperature, "ºC")

print("Se registraron", countHotDays, " días con temperaturas superiores a 30ºC")
print("Se registraron", countColdDays, " días con temperaturas inferiores a 10ºC")
