INSERT_AGE:str = "Introduce edad: "
INSERT_HEIGHT:str = "Introduce altura: "

AGE_ERROR_MESSAGE:str = "La edad debe ser un número entero positivo. Introduce -1 para terminar."
HEIGHT_ERROR_MESSAGE:str = "La altura debe ser mayor que cero."

ACCESS_GRANTED:str = "Acceso permitido"
ACCESS_DENIED:str = "Acceso rechazado"

age:int
height:int

total_guests:int = 0
accepted_guests:int = 0
denied_guests:int = 0

while True:
    try:
        age = int(input(INSERT_AGE))
    except ValueError:
        print(AGE_ERROR_MESSAGE)
        continue

    if age == -1:
        break

    if age < 0:
        print(AGE_ERROR_MESSAGE)
        continue

    while True:
        try:
            height = int(input(INSERT_HEIGHT))
        except ValueError:
            print(HEIGHT_ERROR_MESSAGE)
            continue

        if height > 0:
            break

        print(HEIGHT_ERROR_MESSAGE)


    total_guests += 1

    can_access:bool = age >= 12 and height >= 140
    
    if can_access:
        accepted_guests += 1
        print(ACCESS_GRANTED)
    else:
        denied_guests += 1
        print(ACCESS_DENIED)

print("Visitantes procesados:", total_guests)
print("Visitantes admitidos:", accepted_guests)
print("Visitantes rechazados:", denied_guests)