while True:
    try:
        temperatura: int = int(input("Indica temperatura en celsius:"))
        break
    except ValueError:
        print("Debes escribir un número entero.")

if temperatura < 0:
    print("Hace mucho frío")
elif temperatura <= 10:
    print("Hace frío")
elif temperatura <= 20:
    print("Temperatura suave")
elif temperatura <= 30:
    print("Hace calor")
else:
    print("Hace mucho calor")
